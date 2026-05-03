// =============================================================================
// app/(dashboard)/page.tsx — Dashboard Entry Point
// =============================================================================
// Landing page of the application. Now wrapped by the persistent
// (dashboard)/layout.tsx to prevent layout unmounting on navigation.
// =============================================================================

import { Dashboard } from "@/components/Dashboard";

export default function HomePage() {
  return <Dashboard />;
}
