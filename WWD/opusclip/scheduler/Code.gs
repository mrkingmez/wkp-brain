// Winter Wolf's Den Scheduler v2 (2026-11-04). Pairs with Index.html in this folder.
// SETUP: Project Settings > Script Properties > add OPUS_KEY = your NEW Opus API key.
// Never paste the key into this file. Deploy > Execute as: Me, Who has access: Only myself.

var BASE_URL = 'https://api.opus.pro';

var ACCOUNTS = {
  youtube:   { postAccountId: '6a10fa722ae42657e2924bbf', subAccountId: 'UC2BmJmKYi9JozKblfJ_jHsQ', label: 'YouTube' },
  instagram: { postAccountId: '69a0f3f44df77d215ab34169', subAccountId: '17841480730167044',        label: 'Instagram' },
  facebook:  { postAccountId: '67cd99083a9f32906cd49897', subAccountId: '104052046075172',          label: 'Facebook' }
};

function key_() {
  var k = PropertiesService.getScriptProperties().getProperty('OPUS_KEY');
  if (!k) throw new Error('OPUS_KEY is missing. Add it in Project Settings > Script Properties.');
  return k;
}
function hdr_() { return { 'Authorization': 'Bearer ' + key_(), 'Content-Type': 'application/json' }; }

function doGet() {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('Winter Wolf Den Scheduler')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// ---------- projects ----------
function getSavedProjects() {
  try {
    var raw = PropertiesService.getScriptProperties().getProperty('savedProjects');
    return raw ? JSON.parse(raw) : [];
  } catch (e) { return []; }
}
function getProjects() { return { success: true, projects: getSavedProjects() }; }

function lookupProject(projectId) {
  try {
    var res = UrlFetchApp.fetch(BASE_URL + '/api/exportable-clips?q=findByProjectId&projectId=' + encodeURIComponent(projectId) + '&pageSize=50',
      { method: 'GET', headers: hdr_(), muteHttpExceptions: true });
    if (res.getResponseCode() !== 200) return { success: false, error: 'Could not reach project ' + projectId + ' (API ' + res.getResponseCode() + ')' };
    var data = JSON.parse(res.getContentText());
    var clips = Array.isArray(data) ? data : (data.data || []);
    if (!clips.length) return { success: false, error: 'No clips found for ' + projectId + '. Has Opus Clip finished processing?' };
    var project = { id: projectId, name: clips[0].videoTitle || clips[0].title || ('Project ' + projectId),
                    status: 'COMPLETED', clipCount: clips.length, createdAt: new Date().toISOString() };
    var map = {};
    getSavedProjects().concat([project]).forEach(function (p) { map[p.id] = p; });
    var merged = Object.keys(map).map(function (k) { return map[k]; })
      .sort(function (a, b) { return new Date(b.createdAt) - new Date(a.createdAt); }).slice(0, 20);
    PropertiesService.getScriptProperties().setProperty('savedProjects', JSON.stringify(merged));
    return { success: true, project: project };
  } catch (e) { return { success: false, error: e.message }; }
}

function getClips(projectId) {
  try {
    var res = UrlFetchApp.fetch(BASE_URL + '/api/exportable-clips?q=findByProjectId&projectId=' + encodeURIComponent(projectId) + '&pageSize=50',
      { method: 'GET', headers: hdr_(), muteHttpExceptions: true });
    if (res.getResponseCode() !== 200) return { success: false, error: 'API ' + res.getResponseCode() + ': ' + res.getContentText().slice(0, 200) };
    var data = JSON.parse(res.getContentText());
    var raw = Array.isArray(data) ? data : (data.data || []);
    if (!raw.length) return { success: false, error: 'No clips found. Has Opus Clip finished processing?' };
    var clips = raw.map(function (c) {
      return { id: c.id, projectId: c.projectId, curationId: c.curationId,
               title: c.title || 'Untitled Clip', description: c.description || '',
               score: c.viralityScore || c.score || 0,
               duration: c.durationMs ? Math.round(c.durationMs / 1000) : 0 };
    }).sort(function (a, b) { return b.score - a.score; });
    return { success: true, clips: clips };
  } catch (e) { return { success: false, error: e.message }; }
}

// ---------- schedule log (saved, survives reloads) ----------
function logKey_(projectId) { return 'sched_' + projectId; }
function readLog_(projectId) {
  try { var r = PropertiesService.getScriptProperties().getProperty(logKey_(projectId)); return r ? JSON.parse(r) : []; }
  catch (e) { return []; }
}
function writeLog_(projectId, arr) {
  PropertiesService.getScriptProperties().setProperty(logKey_(projectId), JSON.stringify(arr));
}
// each entry: {s: scheduleId, c: clipId, p: platform, t: publishAt ISO}
function getScheduled(projectId) { return { success: true, items: readLog_(projectId) }; }

// ---------- schedule one post ----------
// description arrives FINAL (approved copy, hashtags already inside it). Nothing is appended here.
function schedulePost(projectId, curationId, platform, publishAtISO, title, description) {
  try {
    var acct = ACCOUNTS[platform];
    if (!acct) return { success: false, error: 'Unknown platform: ' + platform };
    var log = readLog_(projectId);
    for (var i = 0; i < log.length; i++) {
      if (log[i].c === curationId && log[i].p === platform) return { success: false, error: 'Already scheduled (' + platform + '). Cancel it first.' };
    }
    var t = String(title || '');
    if (platform === 'youtube' && t.length > 100) t = t.slice(0, 97) + '...';
    var body = {
      projectId: projectId, clipId: curationId,
      postAccountId: acct.postAccountId, subAccountId: acct.subAccountId,
      publishAt: publishAtISO,
      postDetail: { title: t, mediaType: 'video', custom: { description: description || t, privacy: 'public' } }
    };
    var res = UrlFetchApp.fetch(BASE_URL + '/api/publish-schedules',
      { method: 'POST', headers: hdr_(), payload: JSON.stringify(body), muteHttpExceptions: true });
    var code = res.getResponseCode();
    if (code === 200 || code === 201) {
      var result = JSON.parse(res.getContentText());
      var sid = result.data && result.data.scheduleId;
      if (sid) { log.push({ s: sid, c: curationId, p: platform, t: publishAtISO }); writeLog_(projectId, log); }
      return { success: true, scheduleId: sid };
    }
    return { success: false, error: 'API ' + code + ': ' + res.getContentText().slice(0, 150) };
  } catch (e) { return { success: false, error: e.message }; }
}

// ---------- cancel ----------
function cancelScheduledPost(projectId, scheduleId) {
  try {
    var res = UrlFetchApp.fetch(BASE_URL + '/api/publish-schedules/' + encodeURIComponent(scheduleId),
      { method: 'DELETE', headers: { 'Authorization': 'Bearer ' + key_() }, muteHttpExceptions: true });
    var code = res.getResponseCode();
    if (code === 200 || code === 204 || code === 404) {
      writeLog_(projectId, readLog_(projectId).filter(function (x) { return x.s !== scheduleId; }));
      return { success: true };
    }
    return { success: false, error: 'API ' + code };
  } catch (e) { return { success: false, error: e.message }; }
}
