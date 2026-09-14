// Reads state.json from this same localhost server only. Never calls
// MFL or ESPN directly -- poller.py is the only thing that does that.
const REFRESH_MS = 30000;
let lastFetchAt = null;
let lastFetchOk = false;

async function fetchState() {
  try {
    const resp = await fetch("/state.json", { cache: "no-store" });
    return await resp.json();
  } catch (e) {
    return { error: String(e) };
  }
}

function fmtAge(seconds) {
  if (seconds == null) return "never pulled";
  if (seconds < 60) return `${Math.round(seconds)}s ago`;
  return `${Math.round(seconds / 60)}m ago`;
}

function renderSourceAge(state) {
  document.querySelectorAll(".panel-age").forEach((el) => {
    const src = el.dataset.source;
    const meta = state.sources && state.sources[src];
    if (!meta) {
      el.textContent = "no data source info";
      return;
    }
    el.textContent = `data: ${fmtAge(meta.age_seconds)}${meta.last_error ? " — " + meta.last_error : ""}`;
    el.classList.toggle("stale", !!meta.stale || !!meta.never_succeeded);
  });
}

function renderMatchup(panel) {
  if (!panel || panel.error) {
    document.getElementById("my-score").textContent = "--";
    return;
  }
  const mine = panel.mine, opp = panel.opponent;
  document.getElementById("my-score").textContent = mine.score.toFixed(2);
  document.getElementById("my-proj-mfl").textContent = mine.mfl_projected_final.toFixed(2);
  document.getElementById("my-proj-irfl").textContent = mine.irfl_scoring_projected_final.toFixed(2);
  document.getElementById("my-ytp").textContent = mine.players_yet_to_play;
  document.getElementById("opp-score").textContent = opp.score.toFixed(2);
  document.getElementById("opp-proj-mfl").textContent = opp.mfl_projected_final.toFixed(2);
  document.getElementById("opp-proj-irfl").textContent = opp.irfl_scoring_projected_final.toFixed(2);
  document.getElementById("opp-ytp").textContent = opp.players_yet_to_play;
  document.getElementById("opp-label").textContent = `Franchise ${opp.franchise_id}`;

  const diffEl = document.getElementById("proj-disagreements");
  diffEl.innerHTML = "";
  const threshold = panel.disagreement_threshold_pct || 30;
  const genuine = panel.genuine_disagreements || [];
  const missing = panel.missing_data || [];

  const renderGroup = (label, items, emptyText) => {
    const title = document.createElement("div");
    title.className = "note";
    title.textContent = label;
    diffEl.appendChild(title);
    if (items.length === 0) {
      const row = document.createElement("div");
      row.className = "game-row";
      row.textContent = emptyText;
      diffEl.appendChild(row);
      return;
    }
    items.forEach(d => {
      const row = document.createElement("div");
      row.className = "game-row";
      const reasonText = d.reason ? ` — ${d.reason}` : "";
      row.textContent = `${d.side === "mine" ? "MINE" : "OPP"} — ${d.name} (${d.position || "?"}): `
        + `MFL ${d.mfl_projected} vs IRFL ${d.irfl_scoring_projected} (${d.pct_diff}% apart)${reasonText}`;
      diffEl.appendChild(row);
    });
  };

  renderGroup(
    `Genuine disagreements over ${threshold}% (both sides have a real, non-zero projection):`,
    genuine,
    "None."
  );
  renderGroup(
    `Missing-data cases (one side has no projection at all -- not a scoring disagreement):`,
    missing,
    "None."
  );

  if (panel.unbridged_players && panel.unbridged_players.length) {
    const u = document.createElement("div");
    u.className = "note";
    u.textContent = `${panel.unbridged_players.length} starter(s) have no MFL-to-Sleeper ID match this week -- excluded from the IRFL-scoring total, not silently zeroed.`;
    diffEl.appendChild(u);
  }
  if (panel.kicker_scoring_note) {
    const k = document.createElement("div");
    k.className = "note";
    k.textContent = panel.kicker_scoring_note;
    diffEl.appendChild(k);
  }
}

function renderInactiveBanner(panel) {
  const banner = document.getElementById("inactive-banner");
  const alerts = (panel && panel.alerts) || [];
  if (alerts.length === 0) {
    banner.hidden = true;
    return;
  }
  banner.hidden = false;
  banner.textContent = "INACTIVE ALERT: " + alerts
    .map(a => `${a.name || a.player_id} (${a.position || "?"}) — ${a.status}${a.details ? ": " + a.details : ""}`)
    .join("  |  ");
}

function verdictBadge(verdict) {
  const badge = document.createElement("span");
  badge.className = `verdict-badge ${verdict}`;
  badge.textContent = verdict.replace("_", " ");
  return badge;
}

function renderColorDiscrepancies(discrepancies) {
  const el = document.getElementById("pickem-discrepancies");
  el.innerHTML = "";
  if (!discrepancies || discrepancies.length === 0) {
    el.hidden = true;
    return;
  }
  el.hidden = false;
  const banner = document.createElement("div");
  banner.className = "discrepancy-banner";
  const title = document.createElement("div");
  title.className = "title";
  title.textContent = `${discrepancies.length} color/ESPN disagreement${discrepancies.length > 1 ? "s" : ""} -- card color is a hint, not authoritative:`;
  banner.appendChild(title);
  discrepancies.forEach(d => {
    const line = document.createElement("div");
    line.textContent = `${d.pick_team}: card marked "${d.color_says}" but ESPN's real result is "${d.espn_says}"`;
    banner.appendChild(line);
  });
  el.appendChild(banner);
}

function renderPickemRecord(record) {
  const el = document.getElementById("pickem-record");
  el.innerHTML = "";
  if (!record) return;

  const note = document.createElement("div");
  note.className = "note";
  note.textContent = record.note;
  el.appendChild(note);

  if (record.pick_side_known === true && record.record) {
    const r = record.record;
    const wrap = document.createElement("div");
    wrap.className = "pickem-record";
    let html = `
      <span><span class="rec-num">${r.won}</span> won</span>
      <span><span class="rec-num">${r.lost}</span> lost</span>
      <span><span class="rec-num">${r.undecided}</span> undecided</span>`;
    if (r.unknown_pick > 0) {
      html += `<span><span class="rec-num">${r.unknown_pick}</span> unmarked pick</span>`;
    }
    wrap.innerHTML = html;
    el.appendChild(wrap);
  }
}

function renderPickem(panel) {
  const noteEl = document.getElementById("pickem-note");
  const gamesEl = document.getElementById("pickem-games");
  gamesEl.innerHTML = "";

  if (!panel || panel.card_found === false) {
    noteEl.textContent = panel ? panel.message : "No card data.";
    document.getElementById("pickem-record").innerHTML = "";
    return;
  }

  renderPickemRecord(panel.record);
  renderColorDiscrepancies(panel.color_discrepancies);

  let note = panel.ats_pick_note || "";
  if (panel.no_picks_detected) {
    note += " No Eliminator pick detected either — this card currently reads as fully unmarked.";
  }
  noteEl.textContent = note;

  // Four columns, left to right: MY PICK / GAME / CLOCK / VERDICT.
  // Rebuilt 2026-09-13 -- the old layout gave both teams a
  // covering/not-covering badge (doubled the text, buried the one
  // thing that matters) and marked the actual pick with only a small
  // dot. All four display fields are computed server-side in
  // poller.py's enrich() now, so this is just placement.
  const buildPickRow = (g, prefix) => {
    const row = document.createElement("div");
    row.className = "pick-row";
    if (g.color_discrepancy) row.classList.add("discrepancy");

    const pickCol = document.createElement("div");
    pickCol.className = "col-pick";
    pickCol.textContent = `${prefix}${g.pick_display || "no pick"}`;

    const gameCol = document.createElement("div");
    gameCol.className = "col-game";
    if (g.game_display && g.leader_abbr) {
      const [leftPart, rightPart] = g.game_display.split(" - ");
      const leftIsLeader = leftPart.startsWith(g.leader_abbr + " ");
      const left = document.createElement("span");
      if (leftIsLeader) left.className = "leader";
      left.textContent = leftPart;
      const sep = document.createTextNode(" - ");
      const right = document.createElement("span");
      if (!leftIsLeader) right.className = "leader";
      right.textContent = rightPart;
      gameCol.appendChild(left);
      gameCol.appendChild(sep);
      gameCol.appendChild(right);
    } else {
      gameCol.textContent = g.game_display || (g.match_found ? "" : "no live match found");
    }

    const clockCol = document.createElement("div");
    clockCol.className = "col-clock";
    clockCol.textContent = g.clock_display || "";

    const verdictCol = document.createElement("div");
    verdictCol.className = "col-verdict";
    verdictCol.appendChild(verdictBadge(g.verdict || "NOT_STARTED"));

    row.appendChild(pickCol);
    row.appendChild(gameCol);
    row.appendChild(clockCol);
    row.appendChild(verdictCol);
    return row;
  };

  for (const g of panel.games) {
    gamesEl.appendChild(buildPickRow(g, ""));
  }
  if (panel.tiebreaker) {
    gamesEl.appendChild(buildPickRow(panel.tiebreaker, "MNF: "));
  }
}

function renderScoreboard(panel) {
  const el = document.getElementById("scoreboard-games");
  el.innerHTML = "";
  if (!panel || !panel.games || panel.games.length === 0) {
    el.textContent = "No games currently in progress.";
    return;
  }
  panel.games.forEach(g => {
    const row = document.createElement("div");
    row.className = "scoreboard-row" + (g.on_card ? " on-card" : "");
    const league = document.createElement("span");
    league.className = "league-tag";
    league.textContent = g.league;
    const teams = document.createElement("span");
    teams.textContent = `${g.away_team} ${g.away_score ?? "-"} @ ${g.home_team} ${g.home_score ?? "-"}`;
    const clock = document.createElement("span");
    clock.textContent = `${g.status} ${g.clock || ""}`.trim();
    row.appendChild(league);
    row.appendChild(teams);
    row.appendChild(clock);
    el.appendChild(row);
  });
}

function renderNews(panel) {
  const relEl = document.getElementById("news-relevant");
  const otherEl = document.getElementById("news-other");
  relEl.innerHTML = "";
  otherEl.innerHTML = "";
  if (!panel) return;

  const mk = (h) => {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = h.link;
    a.target = "_blank";
    a.rel = "noopener";
    a.textContent = h.title;
    li.appendChild(a);
    return li;
  };

  (panel.relevant || []).forEach(h => relEl.appendChild(mk(h)));
  (panel.other_collapsed || []).forEach(h => otherEl.appendChild(mk(h)));
  if ((panel.relevant || []).length === 0) {
    const li = document.createElement("li");
    li.textContent = "No roster-relevant headlines right now.";
    relEl.appendChild(li);
  }
}

async function tick() {
  const state = await fetchState();
  if (state.error && !state.panels) {
    document.getElementById("global-meta").textContent = state.error;
    lastFetchOk = false;
    updateDataAge();
    return;
  }
  lastFetchAt = Date.now();
  lastFetchOk = true;
  document.getElementById("global-meta").textContent =
    `Week ${state.week} — ${state.games_live ? "games live" : "no games live, polling paused"} — generated ${state.generated_at}`;

  renderMatchup(state.panels && state.panels.matchup);
  renderInactiveBanner(state.panels && state.panels.inactive_alert);
  renderPickem(state.panels && state.panels.pickem);
  renderScoreboard(state.panels && state.panels.full_scoreboard);
  renderNews(state.panels && state.panels.news);
  renderSourceAge(state);
  updateDataAge();
}

// Prominent corner indicator, ticks every second independent of the
// 30s fetch cycle -- so it's obvious at a glance whether the page is
// alive and how stale state.json is, not just whether JS is running.
function updateDataAge() {
  const el = document.getElementById("data-age");
  if (!lastFetchOk || lastFetchAt === null) {
    el.textContent = "no data";
    el.className = "data-age stale";
    return;
  }
  const ageSec = Math.round((Date.now() - lastFetchAt) / 1000);
  el.textContent = ageSec < 60 ? `updated ${ageSec}s ago` : `updated ${Math.round(ageSec / 60)}m ago`;
  el.className = "data-age" + (ageSec > 120 ? " stale" : ageSec > 45 ? " warn" : "");
}

tick();
setInterval(tick, REFRESH_MS);
setInterval(updateDataAge, 1000);
