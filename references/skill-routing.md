# Skill Routing

Select by deliverable, not by repository name. If a preferred skill is not
available, use the listed fallback while preserving the same artifact contract.

| Stage | Preferred specialist | Required output | Fallback or boundary |
|---|---|---|---|
| problem-framing | `research-paper-writing` when installed | Research brief | Direct structured interview and brief |
| literature-discovery | `nature-academic-search` or `nature-literature-pipeline` | Search log and candidate set | Database/web search with DOI verification |
| deep-reading | `ieee-antennas-reader` for TAP/AWPL antennas; otherwise `nature-paper-card` or `nature-reader` | Paper Cards and literature matrix | Source-grounded manual extraction |
| idea-development | `research-paper-writing` plus relevant domain skill | Ranked research hypotheses | Keep every idea labelled proposed |
| evidence-planning | `ieee-antennas-writing` for antenna claims; otherwise `research-paper-writing` | Claim-evidence map and experiment plan | Direct evidence mapping |
| manuscript-writing | `ieee-antennas-writing` for TAP/AWPL; otherwise `research-paper-writing` | Evidence-bounded draft | Venue-specific official instructions prevail |
| scientific-figures | `nature-figure` for plots and multipanel figures; `scibox-diagram` for editable schematics | Figure brief and final assets | Preserve raw data and editability |
| latex-production | `ieee-antennas-writing` for TAP/AWPL | Buildable manuscript project | Current official venue template |
| review | `nature-reviewer` and `nature-ref-verifier` | Findings and verified references | Separate technical and citation audits |
| humanize | `humanizer` | Natural draft plus fact-diff audit | Style edit only after technical freeze |
| presentation | `nature-paper2ppt`, `presentations`, or Office-PowerPoint-MCP-Server | PPTX and rendered QA | MCP is a separate optional service |

`ChatPaper` may support optional high-recall triage of a large arXiv set, but its
summaries are discovery aids only. Never cite a ChatPaper summary or transfer a
number from it without checking the original paper.

When multiple skills conflict, apply this precedence: user-supplied evidence,
official venue instructions, domain specialist, general writing guidance,
humanizer style preferences.

