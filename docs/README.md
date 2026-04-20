# GenuineNarrativeCreator

A Python sandbox for composing narrative from structured, legible
components — rather than asking a model to improvise it.

## Status

Personal project. Limited commits across years of intermittent attention.
Not a shipped product, not a finished framework, and not competing with
the current crop of LLM-narrative-as-a-service offerings. The code is
me thinking about narrative architecture in a way that prefers
composability over prompt-tuning.

## What the project is exploring

"Genuine" in the name is doing deliberate work. It's an implicit stance
against two things: narrative-by-template (classical procgen that reads
as arbitrary), and narrative-by-black-box (modern LLM wrappers that
read as plausible but are structurally opaque).

What sits in between is narrative as architecture. Lore, character
state, world state, prompt construction, integration with a rendering
or gameplay surface, and feedback-driven adjustment are treated as
named, separable concerns. Any generative layer — whether a templating
engine, a fine-tuned model, or a general LLM — slots into a defined
contract with the rest of the system rather than being the system.

The thesis is that narratives feel genuine when the underlying model
of character, motive, and consequence is consistent — and that
consistency is a property of structure, not of the generator's output
distribution.

This repo predates the "wrap a model and call it a product" era. It
has deliberately not been rewritten as one.

## Current scope

Implemented or scaffolded:

- `narrative/generation` — narrative generation logic, prompt
  construction, and action execution against a world-state
- `narrative/lore` — lore registry keyed to world and character
  identity, intended to hold the invariants a generator must respect
- `core/data_management` — character and world-state management
- `core/feedback` — hooks for feeding gameplay or reader-reaction
  signals back into subsequent generation
- `core/integration` — adapter shapes for game engines (notional
  Pygame and Unity targets)
- `data/` — YAML-backed definitions of characters, dialogue, and world
  state so the inputs are data, not code
- `tests/` — pytest suite exercising the modules in isolation

Not implemented, despite what the directory layout might suggest:

- no runnable game. `main.py` exercises the pipeline; it does not
  render a playable world
- the Pygame and Unity integration points are shapes, not working
  bridges
- the `rtna_advertising` module is scaffolding for exploring how
  narrative-adjacent commercial content (placement, sponsored lore,
  in-world marketing) might be expressed as first-class inputs rather
  than bolted on post-hoc. It is not a revenue system
- the `rtna_user_interface` module is shape for a prospective front
  end; no UI is currently served
- no trained model, no fine-tuning, no model weights shipped with
  the repo

## Running it

Requires Python 3.10+.

    git clone https://github.com/edz314/GenuineNarrativeCreator.git
    cd GenuineNarrativeCreator
    pip install -r docs/requirements.txt
    pytest tests/
    python main.py

`main.py` walks a small scripted scenario through the pipeline —
character and world loaded from `data/`, narrative generated,
feedback hook exercised. It is a demonstration of the wiring, not
a game session.

## Design sketch

Four layers, intentionally separate:

**Lore.** The invariants. What is true about the world and its
characters that any generated narrative must respect. Held as data,
not baked into prose.

**State.** What is true right now. Character attributes, world
observations, active plot threads.

**Generation.** How a specific moment of narrative is produced from
lore, state, and a prompt construction. The generator itself is a
pluggable component — the architecture does not require a particular
model or technique.

**Feedback.** How outcomes (gameplay consequences, reader reactions)
feed back into state and, where warranted, into the generator's
future prompt construction.

The separation matters because it's what lets you swap the generator
— from template-based to LLM-based to something not yet invented —
without the rest of the system changing shape.

## Limitations

- Narrative coherence is asserted by the architecture, not proved by
  it. A generator can still say incoherent things; the framework's
  job is to make that easier to detect and correct, not to prevent
  it.
- No guarantees of scale. The state and lore representations are
  chosen for clarity, not for large casts or long-lived worlds.
- No multiplayer or concurrent-actor modelling.
- The `rtna_advertising` direction is conceptual work in progress.
  If it reads as awkward, that's because it is — the open question
  is whether commercial content belongs inside the narrative model
  or strictly outside it.
- If you want to generate narratives today, wrap an LLM directly.
  This repo is for thinking about what narrative *should look like
  structurally* before the generator does its work.

## License

See `LICENSE`.

- `narrative/generat
