import React from "react";
import {AbsoluteFill, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {loadFont as loadBarlow} from "@remotion/google-fonts/BarlowCondensed";
import {loadFont as loadBask} from "@remotion/google-fonts/LibreBaskerville";
import {theme as T} from "./theme";

loadBarlow("normal", {weights: ["600", "700"]});
loadBask("italic", {weights: ["400"]});

export type End15Props = {showBadge: boolean; showGuides: boolean};
const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
const ease = (f: number, a: number, b: number, e = T.ease.out) => interpolate(f, [a, b], [0, 1], {...clamp, easing: e});

// words: single source is D:\WKP\Post-Production\projects\ian-trailer\end-15s\words-end-15s.md
const W = {
  the: "THE", title: "WRENCH TURNER", sub: "A CONTEMPORARY FAMILY DRAMA",
  badge1: "2026 PENMASTERS GLOBAL", badge2: "FICTION AWARDS FINALIST", badge3: "GENERAL FICTION",
  avail: "AVAILABLE NOW", amazon: "READ IT ON AMAZON", link: "a.co/d/06dqYpQw",
  author: "IAN GRIFFIN", army: "U.S. ARMY, 31 YEARS",
  quote: "I am just an old soldier who relishes writing about the complexities of life.",
  tag: "THE WRENCH TURNER",
};

const Grit: React.FC = () => (
  <svg width="0" height="0" style={{position: "absolute"}}>
    <defs>
      <filter id="grit" x="-5%" y="-5%" width="110%" height="110%">
        <feTurbulence type="fractalNoise" baseFrequency="0.6" numOctaves="2" seed="7" result="n" />
        <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -6 4.7" result="m" />
        <feComposite in="SourceGraphic" in2="m" operator="in" />
      </filter>
      <filter id="gritLight" x="-5%" y="-5%" width="110%" height="110%">
        <feTurbulence type="fractalNoise" baseFrequency="0.6" numOctaves="2" seed="3" result="n" />
        <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -5 4.3" result="m" />
        <feComposite in="SourceGraphic" in2="m" operator="in" />
      </filter>
    </defs>
  </svg>
);

const Backdrop: React.FC<{dim?: number}> = ({dim = 1}) => {
  const f = useCurrentFrame();
  const flick = 0.94 + 0.06 * Math.sin(f / 7) * Math.sin(f / 3.1);
  return (
    <AbsoluteFill style={{background: T.colors.bg}}>
      <AbsoluteFill style={{background: `radial-gradient(ellipse 60% 70% at 78% 12%, rgba(232,163,61,${0.34 * flick * dim}) 0%, rgba(200,86,31,${0.12 * dim}) 45%, transparent 75%)`}} />
      <AbsoluteFill style={{background: `radial-gradient(ellipse 50% 50% at 8% 95%, rgba(200,86,31,${0.16 * dim}) 0%, transparent 70%)`}} />
      <AbsoluteFill style={{opacity: 0.07, backgroundImage: "repeating-linear-gradient(90deg, #fff 0 1px, transparent 1px 96px), repeating-linear-gradient(0deg, #fff 0 1px, transparent 1px 96px)"}} />
    </AbsoluteFill>
  );
};

const Finish: React.FC = () => {
  const f = useCurrentFrame();
  const seed = Math.floor(f / 2) % 12;
  const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' seed='${seed}'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>`;
  return (
    <>
      <AbsoluteFill style={{background: "radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,0.65) 100%)"}} />
      <AbsoluteFill style={{opacity: 0.1, mixBlendMode: "overlay", backgroundImage: `url("data:image/svg+xml;utf8,${svg}")`}} />
    </>
  );
};

const rise = (f: number, start: number, dur = 16) => {
  const p = ease(f, start, start + dur);
  return {opacity: p, transform: `translateY(${(1 - p) * 40}px) scale(${0.96 + 0.04 * p})`};
};

const Flag: React.FC<{w?: number}> = ({w = 54}) => {
  const h = (w * 10) / 19;
  return (
    <svg width={w} height={h} viewBox="0 0 190 100" style={{display: "block"}}>
      {Array.from({length: 13}).map((_, i) => <rect key={i} y={(i * 100) / 13} width="190" height={100 / 13 + 0.5} fill={i % 2 === 0 ? "#B22234" : "#F4F4F4"} />)}
      <rect width="76" height={(100 * 7) / 13} fill="#3C3B6E" />
      {Array.from({length: 5}).map((_, r) => Array.from({length: r % 2 ? 4 : 5}).map((__, c) => <circle key={`${r}${c}`} cx={(r % 2 ? 15 : 7.5) + c * 15} cy={7.5 + r * 14} r="3" fill="#F4F4F4" />))}
    </svg>
  );
};

const Sales: React.FC<{showBadge: boolean}> = ({showBadge}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const colX = 860;

  const coverS = spring({frame: f - 4, fps, config: T.spring.smooth});
  const breathe = 1 + 0.006 * Math.sin(f / 18);
  const coverGlow = 0.35 + 0.15 * Math.sin(f / 14);

  const sf = f - 84;
  const slam = spring({frame: Math.max(0, sf), fps, config: T.spring.slam});
  const stampScale = sf < 0 ? 3 : 1 + (1 - slam) * 1.6;
  const stampBlur = sf < 0 ? 12 : Math.max(0, (1 - slam) * 14);
  const stampOp = sf < 0 ? 0 : Math.min(1, sf / 2);
  const shake = sf >= 0 && sf < 7 ? Math.sin(sf * 4) * (7 - sf) * 1.4 : 0;
  const flash = sf >= 0 && sf < 4 ? 0.28 * (1 - sf / 4) : 0;

  const bs = spring({frame: Math.max(0, f - 58), fps, config: T.spring.snappy});
  const bOp = f < 58 ? 0 : Math.min(1, bs);

  const lp = ease(f, 118, 136);
  const sweep = ease(f, 134, 160, T.ease.inOut);
  const lglow = 0.5 + 0.5 * Math.sin((f - 130) / 9);

  const fadeIn = ease(f, 0, 8);
  const exit = 1 - ease(f, 180, 191, T.ease.in);

  return (
    <AbsoluteFill style={{opacity: fadeIn * exit}}>
      <Backdrop />
      <div style={{position: "absolute", inset: 0, background: `rgba(255,190,100,${flash})`}} />
      <div style={{position: "absolute", left: 150, top: 140, width: 533, height: 800, opacity: Math.min(1, coverS * 1.4),
        transform: `translateX(${(1 - coverS) * -90}px) scale(${(0.92 + 0.08 * coverS) * breathe}) rotate(${(1 - coverS) * -3}deg)`,
        boxShadow: `0 30px 80px rgba(0,0,0,0.75), 0 0 ${90 * coverGlow}px rgba(232,163,61,${coverGlow})`}}>
        <Img src={staticFile("cover.jpg")} style={{width: "100%", height: "100%", objectFit: "contain", display: "block"}} />
      </div>

      <div style={{position: "absolute", left: colX, top: 110, fontFamily: T.fonts.display, fontWeight: 700, textTransform: "uppercase"}}>
        <div style={{...rise(f, 18), fontSize: 64, letterSpacing: 18, color: T.colors.steel, filter: "url(#gritLight)"}}>{W.the}</div>
        <div style={{...rise(f, 24), fontSize: 150, lineHeight: 0.95, letterSpacing: 4, color: T.colors.steel, filter: "url(#grit)", marginTop: -4}}>{W.title}</div>
        <div style={{width: 940 * ease(f, 40, 62, T.ease.inOut), height: 4, background: T.colors.amber, marginTop: 14, boxShadow: `0 0 14px ${T.colors.amber}`}} />
        <div style={{...rise(f, 46), fontSize: 38, letterSpacing: 9, color: T.colors.amber, marginTop: 16, fontWeight: 600}}>{W.sub}</div>
      </div>

      {showBadge && (
        <div style={{position: "absolute", left: colX, top: 432, opacity: bOp, transform: `translateX(${(1 - bs) * 60}px) scale(${0.9 + 0.1 * bs})`,
          border: `3px solid ${T.colors.amber}`, borderRadius: 8, padding: "12px 26px", background: "rgba(20,12,6,0.72)", boxShadow: "0 0 28px rgba(232,163,61,0.25)",
          fontFamily: T.fonts.display, textTransform: "uppercase", display: "flex", alignItems: "center", gap: 22}}>
          <div style={{fontSize: 74, color: T.colors.amber, lineHeight: 1, fontWeight: 700}}>{"\u2605"}</div>
          <div>
            <div style={{fontSize: 36, fontWeight: 700, letterSpacing: 3, color: T.colors.text, lineHeight: 1.05}}>{W.badge1}</div>
            <div style={{fontSize: 36, fontWeight: 700, letterSpacing: 3, color: T.colors.text, lineHeight: 1.05}}>{W.badge2}</div>
            <div style={{fontSize: 26, fontWeight: 600, letterSpacing: 6, color: T.colors.amber, marginTop: 2}}>{W.badge3}</div>
          </div>
        </div>
      )}

      <div style={{position: "absolute", left: colX + 10, top: 602, opacity: stampOp,
        transform: `translate(${shake}px, ${-shake * 0.6}px) rotate(-5deg) scale(${stampScale})`, transformOrigin: "30% 50%", filter: `blur(${stampBlur}px) drop-shadow(0 8px 10px rgba(0,0,0,0.6))`}}>
        <div style={{filter: "url(#grit)"}}>
          <div style={{border: `9px solid ${T.colors.stampRed}`, borderRadius: 10, padding: "4px 24px", fontFamily: T.fonts.display, fontWeight: 700, fontSize: 128, lineHeight: 1.0, letterSpacing: 6, color: T.colors.stampRed, textTransform: "uppercase", background: "rgba(194,31,31,0.07)"}}>
            {W.avail}
          </div>
        </div>
      </div>

      <div style={{position: "absolute", left: colX, top: 836, opacity: lp, transform: `translateY(${(1 - lp) * 30}px)`, fontFamily: T.fonts.display, textTransform: "uppercase"}}>
        <div style={{fontSize: 30, letterSpacing: 9, color: T.colors.steelDim, fontWeight: 600}}>{W.amazon}</div>
        <div style={{position: "relative", display: "inline-block", marginTop: 6, padding: "6px 30px", border: `3px solid ${T.colors.amber}`, borderRadius: 6, background: "rgba(232,163,61,0.10)", boxShadow: `0 0 ${14 + 26 * lglow}px rgba(232,163,61,${0.2 + 0.25 * lglow})`, overflow: "hidden"}}>
          <span style={{fontSize: 82, fontWeight: 700, letterSpacing: 3, color: T.colors.amberHot, textTransform: "none"}}>{W.link}</span>
          <div style={{position: "absolute", top: 0, bottom: 0, left: `${-30 + sweep * 150}%`, width: "22%", background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.35), transparent)", transform: "skewX(-20deg)"}} />
        </div>
      </div>
    </AbsoluteFill>
  );
};

const Author: React.FC = () => {
  const f = useCurrentFrame();
  const push = interpolate(f, [0, 168], [1, 1.05], {...clamp, easing: T.ease.inOut});
  const pf = ease(f, 0, 14);
  const words = W.quote.split(" ");
  const wStart = 30;
  const tagP = ease(f, 118, 134);
  return (
    <AbsoluteFill>
      <Backdrop dim={0.85} />
      <div style={{position: "absolute", left: 200, top: 80, width: 550, height: 920, opacity: pf, boxShadow: "0 30px 80px rgba(0,0,0,0.75), 0 0 60px rgba(232,163,61,0.22)", transform: `scale(${push})`, transformOrigin: "50% 50%"}}>
        <Img src={staticFile("author-banner.jpg")} style={{width: "100%", height: "100%", objectFit: "contain", display: "block"}} />
      </div>
      <div style={{position: "absolute", left: 860, top: 150, width: 964}}>
        <div style={{...rise(f, 10), fontFamily: T.fonts.display, fontWeight: 700, fontSize: 150, letterSpacing: 8, color: T.colors.steel, filter: "url(#grit)", lineHeight: 1}}>{W.author}</div>
        <div style={{...rise(f, 18), display: "flex", alignItems: "center", gap: 20, marginTop: 14}}>
          <Flag w={64} />
          <div style={{fontFamily: T.fonts.display, fontWeight: 600, fontSize: 44, letterSpacing: 8, color: T.colors.amber}}>{W.army}</div>
        </div>
        <div style={{width: 760 * ease(f, 22, 44, T.ease.inOut), height: 4, background: T.colors.amber, marginTop: 22, boxShadow: `0 0 14px ${T.colors.amber}`}} />
        <div style={{marginTop: 44, fontFamily: T.fonts.serif, fontStyle: "italic", fontSize: 52, lineHeight: 1.42, color: T.colors.text}}>
          {words.map((w, i) => {
            const p = ease(f, wStart + i * 3, wStart + i * 3 + 12);
            return <span key={i} style={{display: "inline-block", opacity: p, transform: `translateY(${(1 - p) * 18}px)`, marginRight: i === words.length - 1 ? 0 : 14}}>{i === 0 && <span style={{color: T.colors.amber}}>{"“"}</span>}{w}{i === words.length - 1 && <span style={{color: T.colors.amber}}>{"”"}</span>}</span>;
          })}
        </div>
        <div style={{marginTop: 54, opacity: tagP, transform: `translateY(${(1 - tagP) * 20}px)`, fontFamily: T.fonts.display, fontWeight: 600, fontSize: 38, letterSpacing: 8, color: T.colors.steel}}>
          {W.tag} <span style={{color: T.colors.amber}}>{"·"}</span> <span style={{color: T.colors.stampRed, fontWeight: 700}}>{W.avail}</span>
          <div style={{textTransform: "none", letterSpacing: 3, color: T.colors.amberHot, fontSize: 52, marginTop: 6}}>{W.link}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const End15: React.FC<End15Props> = ({showBadge, showGuides}) => {
  const f = useCurrentFrame();
  const aIn = ease(f, 186, 192, T.ease.inOut);
  return (
    <AbsoluteFill style={{background: T.colors.bg}}>
      <Grit />
      <Sequence from={0} durationInFrames={192}><Sales showBadge={showBadge} /></Sequence>
      <Sequence from={186}><AbsoluteFill style={{opacity: aIn}}><Author /></AbsoluteFill></Sequence>
      <Finish />
      {showGuides && (
        <AbsoluteFill style={{pointerEvents: "none"}}>
          <div style={{position: "absolute", left: 96, right: 96, top: 54, bottom: 54, border: "2px dashed rgba(0,255,255,0.7)"}} />
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
