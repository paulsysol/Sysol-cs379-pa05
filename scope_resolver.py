"""
PA 5: The Scope Resolver -- starter.

Complete resolve_name below. See the assignment, Part B,
for the full requirements.
"""

from typing import List

from symtable import Environment, SemanticError


def resolve_name(
    name: str,
    current_env: Environment,
    call_stack: List[Environment],
    mode: str,
) -> int:
    """
    Return the declaration line `name` resolves to.

    mode == "static": climb current_env.parent links (ignore call_stack).
    mode == "dynamic": search call_stack from most-recent (index -1)
        to oldest (index 0), checking each caller's OWN locally-defined
        names only (not their parents), falling back to the global
        (outermost lexical) environment if not found on the stack.
    Any other mode raises ValueError. Raise SemanticError if `name`
    cannot be resolved under the requested mode.
    """
    # TODO
    if mode == "static":
        try:
            return current_env.resolve(name)
        except SemanticError:
            raise SemanticError(f"Variable '{name}' is undefined using static scoping")
    elif mode == "dynamic":
         for cs in reversed(call_stack):
            try:
                return cs.resolve(name)
            except SemanticError:   # variable undefined in this scope, check the next
                pass
         if isinstance(current_env.parent, Environment):     # global scope
            try:
                return current_env.parent.resolve(name)
            except SemanticError:
                raise SemanticError(f"Variable '{name}' is undefined using dynamic scoping")
    else:
        raise ValueError(f"{mode} is not a valid scope mode.")
