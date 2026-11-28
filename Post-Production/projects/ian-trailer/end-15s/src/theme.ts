import {Easing} from "remotion";
export const theme = {
  colors: {
    bg: "#0b0907", amber: "#E8A33D", amberHot: "#FFC766", ember: "#C8561F",
    steel: "#C4C7C9", steelDim: "#8E9396", stampRed: "#C21F1F", text: "#F3ECE2",
  },
  fonts: {display: "Barlow Condensed", serif: "Libre Baskerville"},
  ease: {out: Easing.bezier(0.16, 1, 0.3, 1), inOut: Easing.bezier(0.83, 0, 0.17, 1), in: Easing.bezier(0.7, 0, 0.84, 0)},
  spring: {snappy: {damping: 14, stiffness: 160, mass: 0.6}, smooth: {damping: 20, stiffness: 90, mass: 1}, slam: {damping: 9, stiffness: 260, mass: 0.7}},
} as const;
