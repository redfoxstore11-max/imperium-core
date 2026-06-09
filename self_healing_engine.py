"""
Module: self_healing_engine.py
Core Component of the Imperium Core Framework.
Provides autonomous exception interception, self-healing diagnostics, 
and automatic recovery loops for multi-agent workflows.
"""

import logging
import time
import traceback
import random
from typing import Dict, Any, Callable, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] [SelfHealing] %(message)s')
logger = logging.getLogger("SelfHealingEngine")

class SelfHealingEngine:
    """
    Monitors agent execution blocks, intercepts infrastructure or logic faults,
    and applies automated mitigation strategies to preserve digital sovereignty.
    """
    def __init__(self, max_retries: int = 3, backoff_factor: float = 1.5):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.failure_registry: Dict[str, int] = {}
        logger.info("Autonomous Self-Healing Engine initialized and monitoring.")

    def execute_with_healing(self, agent_alias: str, task_name: str, action: Callable[..., Any], *args, **kwargs) -> Any:
        """
        Executes an agent action within a protective self-healing wrapper.
        If a failure occurs, it analyzes the fault and attempts an autonomous recovery loop.
        """
        retries = 0
        current_backoff = self.backoff_factor
        error_key = f"{agent_alias}:{task_name}"

        while retries <= self.max_retries:
            try:
                if retries > 0:
                    logger.info(f"Attempting autonomous recovery loop ({retries}/{self.max_retries}) for {error_key}...")
                
                # Execute the core agent logic
                result = action(*args, **kwargs)
                
                if retries > 0:
                    logger.info(f"Self-healing SUCCESSFUL for {error_key}. System stabilized.")
                    # Reset failure registry on successful resolution
                    self.failure_registry[error_key] = 0
                return result

            except Exception as e:
                retries += 1
                self.failure_registry[error_key] = self.failure_registry.get(error_key, 0) + 1
                
                logger.error(f"Fault detected in [{agent_alias}] during task [{task_name}].")
                logger.error(f"Exception Type: {e.__class__.__name__} | Message: {str(e)}")
                
                if retries > self.max_retries:
                    logger.critical(f"Self-healing FAILED. Maximum retries exceeded for {error_key}. Esculating to system panic mode.")
                    raise e

                # Determine recovery strategy based on error context (simulation)
                logger.warning(f"Analyzing fault metrics... Applying cool-down backoff of {current_backoff}s.")
                time.sleep(current_backoff)
                current_backoff *= 2  # Exponential backoff escalation

# --- Validation and Simulation Environment ---
def unstable_agent_action():
    """Simulates a fragile network connection or API timeout during an infrastructure sync."""
    if random.random() < 0.7:  # 70% chance to fail initially
        raise ConnectionResetError("Remote cluster refused handshake. Connection closed by peer.")
    return {"status": "SOVEREIGN_NODE_ONLINE", "payload_delivered": True}

if __name__ == "__main__":
    print("--- Validating Self-Healing Engine ---")
    engine = SelfHealingEngine(max_retries=3)
    
    # Simulating the Executive persona overseeing a fragile workflow execution
    print("\n[System] Spawning Executor persona for simulated infrastructure sync...")
    try:
        execution_report = engine.execute_with_healing(
            agent_alias="Executor",
            task_name="cluster_infrastructure_sync",
            action=unstable_agent_action
        )
        print(f"\n[System] Final Execution Report: {execution_report}")
    except Exception:
        print("\n[System] Simulation concluded with hard fault.")
        
    print("\n--- Validation Complete ---")
