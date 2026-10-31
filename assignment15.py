import gc
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.cycle = None

    def __del__(self):
        """Triggers automatically when Python drops this object from memory."""
        print(f"🗑️ Memory Freed: Node '{self.name}' has been destroyed.")

def create_isolated_cycle():
    print("\n--- Step 1: Creating objects & establishing a cycle ---")
    node_a = Node("A")
    node_b = Node("B")
    
    # Create the cyclic cross-reference
    node_a.cycle = node_b
    node_b.cycle = node_a
    
    print("Variables are going out of scope now...")
    # Both variables disappear, but their cross-references keep reference counts > 0

if __name__ == "__main__":
    # Disable automatic collection briefly to isolate our experiment
    gc.disable()
    
    create_isolated_cycle()
    
    # Look for unreachable (but uncollected) items
    print(f"Unreachable objects found before manual collection: {len(gc.garbage)}")
    
    print("\n--- Step 2: Triggering manual garbage collection ---")
    # Force collection on Generation 2 (all generations)
    unreachable_count = gc.collect() 
    
    print(f"GC successfully swept and cleared {unreachable_count} isolated objects.")
    
    # Turn automatic garbage collection back on
    gc.enable()
    print("\n--- Experiment Finished ---")
