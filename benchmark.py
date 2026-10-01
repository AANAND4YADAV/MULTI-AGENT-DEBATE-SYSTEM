"""
Latency Benchmarking Utility for MULTI-AGENT-DEBATE-SYSTEM (MADS)

This module provides a LatencyBenchmark class to measure and analyze
the performance of agent responses during debate sessions.
"""

import time
import statistics
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class LatencyMetrics:
    """Container for latency benchmark metrics."""
    total_latency: float
    mean_latency: float
    average_latency_per_turn: float
    p95_percentile: float
    min_latency: float
    max_latency: float
    num_turns: int
    
    def __str__(self) -> str:
        """Format metrics as a readable string."""
        return (
            f"\n{'='*50}\n"
            f"LATENCY BENCHMARK METRICS\n"
            f"{'='*50}\n"
            f"Total Latency:           {self.total_latency:.4f}s\n"
            f"Mean Latency:            {self.mean_latency:.4f}s\n"
            f"Avg Latency per Turn:    {self.average_latency_per_turn:.4f}s\n"
            f"P95 Percentile Latency:  {self.p95_percentile:.4f}s\n"
            f"Min Latency:             {self.min_latency:.4f}s\n"
            f"Max Latency:             {self.max_latency:.4f}s\n"
            f"Number of Turns:         {self.num_turns}\n"
            f"{'='*50}\n"
        )
    
    def to_dict(self) -> Dict[str, float]:
        """Convert metrics to dictionary for logging/export."""
        return {
            "total_latency_s": self.total_latency,
            "mean_latency_s": self.mean_latency,
            "average_latency_per_turn_s": self.average_latency_per_turn,
            "p95_percentile_latency_s": self.p95_percentile,
            "min_latency_s": self.min_latency,
            "max_latency_s": self.max_latency,
            "num_turns": self.num_turns,
        }


class LatencyBenchmark:
    """
    Utility class for measuring and analyzing latency metrics in agent debates.
    
    Stores elapsed times and provides methods to calculate:
    1. Total end-to-end latency
    2. Mean latency
    3. Average latency per agent turn
    4. P95 percentile latency
    5. Min/Max latency
    
    Example:
        >>> benchmark = LatencyBenchmark()
        >>> start = benchmark.start_timer()
        >>> # ... agent response code ...
        >>> benchmark.record_latency(start)
        >>> metrics = benchmark.calculate_metrics(num_agents=3)
        >>> print(metrics)
    """
    
    def __init__(self, name: str = "Default Debate"):
        """
        Initialize the LatencyBenchmark.
        
        Args:
            name: Name/label for this benchmark session
        """
        self.name = name
        self.latencies: List[float] = []
        self.session_start: Optional[float] = None
    
    def start_session(self) -> float:
        """
        Mark the start of a benchmark session.
        
        Returns:
            Start time from time.perf_counter()
        """
        self.session_start = time.perf_counter()
        return self.session_start
    
    def start_timer(self) -> float:
        """
        Start a timer for an individual agent response.
        
        Returns:
            Current time from time.perf_counter()
        """
        return time.perf_counter()
    
    def record_latency(self, start_time: float) -> float:
        """
        Record latency for a completed agent response.
        
        Args:
            start_time: The start time returned by start_timer()
            
        Returns:
            Elapsed time in seconds
        """
        elapsed = time.perf_counter() - start_time
        self.latencies.append(elapsed)
        return elapsed
    
    def get_total_latency(self) -> float:
        """
        Get total end-to-end latency from session start to now.
        
        Returns:
            Total elapsed time in seconds, or 0 if session not started
        """
        if self.session_start is None:
            return 0.0
        return time.perf_counter() - self.session_start
    
    def get_mean_latency(self) -> float:
        """
        Get mean (average) latency across all recorded turns.
        
        Returns:
            Mean latency in seconds, or 0 if no latencies recorded
        """
        if not self.latencies:
            return 0.0
        return statistics.mean(self.latencies)
    
    def get_average_latency_per_turn(self, num_agents: int = 1) -> float:
        """
        Get average latency per agent turn.
        
        Args:
            num_agents: Number of agents participating in the debate
            
        Returns:
            Average latency per turn in seconds
        """
        if not self.latencies or num_agents <= 0:
            return 0.0
        total_turns = len(self.latencies)
        turns_per_agent = max(1, total_turns // num_agents)
        return self.get_mean_latency() / turns_per_agent if turns_per_agent > 0 else 0.0
    
    def get_p95_percentile(self) -> float:
        """
        Get 95th percentile latency.
        
        Returns:
            P95 latency in seconds, or 0 if insufficient data
        """
        if len(self.latencies) < 2:
            return 0.0
        return statistics.quantiles(self.latencies, n=20)[18]  # 19/20 = 0.95
    
    def get_min_max_latency(self) -> Tuple[float, float]:
        """
        Get minimum and maximum latency.
        
        Returns:
            Tuple of (min_latency, max_latency), or (0, 0) if no data
        """
        if not self.latencies:
            return (0.0, 0.0)
        return (min(self.latencies), max(self.latencies))
    
    def calculate_metrics(self, num_agents: int = 1) -> LatencyMetrics:
        """
        Calculate all latency metrics at once.
        
        Args:
            num_agents: Number of agents in the debate session
            
        Returns:
            LatencyMetrics object containing all 5 metrics
        """
        min_lat, max_lat = self.get_min_max_latency()
        
        return LatencyMetrics(
            total_latency=self.get_total_latency(),
            mean_latency=self.get_mean_latency(),
            average_latency_per_turn=self.get_average_latency_per_turn(num_agents),
            p95_percentile=self.get_p95_percentile(),
            min_latency=min_lat,
            max_latency=max_lat,
            num_turns=len(self.latencies),
        )
    
    def reset(self) -> None:
        """Clear all recorded latencies and session start time."""
        self.latencies = []
        self.session_start = None
    
    def get_statistics(self) -> Dict[str, float]:
        """
        Get additional statistics about recorded latencies.
        
        Returns:
            Dictionary with additional stats (stdev, median, etc.)
        """
        if not self.latencies:
            return {}
        
        return {
            "median": statistics.median(self.latencies),
            "stdev": statistics.stdev(self.latencies) if len(self.latencies) > 1 else 0.0,
            "variance": statistics.variance(self.latencies) if len(self.latencies) > 1 else 0.0,
        }


# Example usage and integration
if __name__ == "__main__":
    """
    Example: Benchmarking a debate session with 3 agents
    """
    import random
    
    print("MADS Latency Benchmark Example")
    print("-" * 50)
    
    # Create benchmark instance
    benchmark = LatencyBenchmark(name="Sample Debate Session")
    benchmark.start_session()
    
    # Simulate 9 agent responses (3 agents, 3 turns each)
    num_agents = 3
    turns_per_agent = 3
    
    for turn in range(turns_per_agent):
        for agent_id in range(num_agents):
            # Start timer for agent response
            start = benchmark.start_timer()
            
            # Simulate agent processing time (0.1 to 0.5 seconds)
            time.sleep(random.uniform(0.1, 0.5))
            
            # Record latency
            latency = benchmark.record_latency(start)
            print(f"Agent {agent_id+1}, Turn {turn+1}: {latency:.4f}s")
    
    # Calculate metrics
    metrics = benchmark.calculate_metrics(num_agents=num_agents)
    print(metrics)
    
    # Get additional statistics
    stats = benchmark.get_statistics()
    print("Additional Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:.4f}s")
    
    # Export to dictionary
    print("\nExport as Dictionary:")
    print(metrics.to_dict())
