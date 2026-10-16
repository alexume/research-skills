# Evidence Discovery Strategy

## Search matrix

Construct one row per requirement and repository family:

| Requirement | Source family | Repository or catalogue | Query concepts | Coverage filter | Status |
|---|---|---|---|---|---|

Search concepts should include contemporary and historical place names, institutional names, classification terms, abbreviations, languages, and spelling variants. Keep the design concept separate from the vocabulary used by source producers.

## Repository sequence

Prefer:

1. producing institution or archive;
2. official repository or catalogue;
3. trusted disciplinary or national repository;
4. verified mirror with provenance;
5. broad discovery services used to locate the above.

Useful discovery infrastructure may include official statistical portals, national and regional archives, library catalogues, DataCite records, domain repositories, and documented scholarly graph APIs. Always verify the final record at the provider or custodian.

Official documentation:

- DataCite APIs: https://support.datacite.org/docs/api
- OpenAlex documentation: https://docs.openalex.org/

## Stopping rules

Define stopping before extensive search. A defensible stopping memo records:

- all priority repository families searched;
- languages and historical names used;
- date and coverage filters;
- backward and forward provenance chains followed;
- duplicate, inaccessible, rejected, and partial results;
- remaining probability that another source would change feasibility.

Stop when the requirement is satisfied, when documented search saturation is reached, or when further search exceeds the project's resource constraint. Never stop merely because the first usable file was found.

## Search logs

`project/evidence_discovery_log.csv` should include:

- requirement and search identifiers;
- platform or repository;
- exact query and filters;
- search date and language;
- result count reviewed;
- candidate stable identifiers;
- disposition and reason;
- next search action or stopping reason.
