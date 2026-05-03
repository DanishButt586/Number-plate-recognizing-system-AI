// =============================================================================
// components/layout/DashboardLayout.tsx — Main Dashboard Shell
// =============================================================================
// Composition component that wraps Sidebar + Topbar + main content area.
// Handles health polling (checks backend every 30s), sidebar toggle state,
// and passes status down to child components.
// =============================================================================

"use client";

import { useState } from "react";
import { Sidebar } from "./Sidebar";
import { Topbar } from "./Topbar";
import { useHealthStatus } from "@/hooks/useHealth";

interface DashboardLayoutProps {
  children: React.ReactNode;
}

export function DashboardLayout({ children }: DashboardLayoutProps) {
  const { data: health, isError } = useHealthStatus();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // Derive online status from health data
  const isOnline = !!health && !isError;

  return (
    <div className="flex min-h-screen bg-neutral-950">
      {/* Sidebar — fixed on desktop, drawer on mobile */}
      <Sidebar
        health={health ?? null}
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      {/* Main content — offset by sidebar width on desktop */}
      <div className="flex flex-1 flex-col lg:pl-64">
        <Topbar
          isOnline={isOnline}
          onMenuToggle={() => setSidebarOpen((prev) => !prev)}
        />
        <main className="flex-1 p-4 sm:p-6 lg:p-8">{children}</main>
      </div>
    </div>
  );
}
