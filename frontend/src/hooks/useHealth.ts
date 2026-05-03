import { useQuery } from "@tanstack/react-query";
import { checkHealth } from "@/services/anprService";
import type { HealthResponse } from "@/types";

/**
 * Hook to monitor backend health and model status.
 * Uses React Query for automatic polling and caching.
 */
export function useHealthStatus() {
  return useQuery<HealthResponse>({
    queryKey: ["health"],
    queryFn: checkHealth,
    refetchInterval: 30000, // Poll every 30 seconds
    staleTime: 10000,      // Consider fresh for 10 seconds
    retry: 3,
  });
}
