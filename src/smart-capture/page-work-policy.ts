import type { SmartCaptureExecutionContext } from "./orchestrator";

export function shouldSampleRecordingOnStop(
  context?: SmartCaptureExecutionContext,
  now = performance.now()
) {
  if (!context) return true;
  return !context.signal.aborted
    && context.safetyLevel !== "snapshot-only"
    && context.safetyLevel !== "stopped"
    && now < context.deadline;
}
