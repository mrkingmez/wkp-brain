import React from "react";
import {Composition} from "remotion";
import {End15, End15Props} from "./End15";
export const Root: React.FC = () => (
  <Composition
    id="End15-16x9" component={End15} durationInFrames={360} fps={24} width={1920} height={1080}
    defaultProps={{showBadge: true, showGuides: false} as End15Props}
  />
);
