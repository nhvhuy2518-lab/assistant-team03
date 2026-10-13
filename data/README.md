# Data Sources and Ownership

This directory contains data files used by the assistant to answer office-related questions.

## Data files

| File | Purpose | Source | Owner | Update frequency |
|---|---|---|---|---|
| `offices.csv` | Stores office names, room locations, and opening hours | Public HCMUS university websites and contact pages; see the source notes below | Member 3 (`@kknguyen2532-lab`) | Review once per semester and whenever an official source changes |

The update frequency is the team's maintenance policy, not an official university schedule.

## Public sources

The following public sources are used to verify office information:

| Office | Source |
|---|---|
| Graduate Training Office | https://sdh.hcmus.edu.vn/lien-he/ |
| Office of External Relations | https://hcmus.edu.vn/phong-quan-he-doi-ngoai/ |
| Office of Inspection and Legal Affairs | https://ttpc.hcmus.edu.vn/ |
| Office of Undergraduate Training | https://hcmus.edu.vn/phong-dao-tao/ |
| Office of Planning and Finance | https://hcmus.edu.vn/phong-ke-hoach-tai-chinh/ |
| Office of Information and Communications | https://hcmus.edu.vn/phong-thong-tin-truyen-thong/ |

A listed website is a starting point for verification; it does not mean every room number or opening hour in the CSV has been confirmed.

## Data quality and maintenance

- Keep the CSV header as `name,room,hours`.
- Use UTF-8 encoding and valid CSV formatting.
- Keep office names unique.
- Do not invent room numbers or opening hours.
- Use `Not published` when a value has not been verified from a public source.
- Review the official source pages once per semester and whenever a relevant change is announced.
- The original sample records retained in `offices.csv` have not been independently verified against official sources.
- Before updating a record, check the source and record the date of verification in the pull request description.

## Ownership

Member 3 is responsible for documenting the sources, checking data quality, and proposing updates. Changes to the dataset must go through the team's normal branch, pull request, and review process.