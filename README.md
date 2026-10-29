# Hello Portal

A Python 3.12 / FastAPI sample for the live portal ZIP onboarding walkthrough.

## Run and test locally

```sh
uv sync --locked
uv run --locked pytest -q
uv run --locked ruff check .
uv run --locked uvicorn app.main:app --host 127.0.0.1 --port 8000
```

The homepage is `/`, the API is `/api/message`, and health is `/health`.
Development and production requirements are hash-locked separately. The Dockerfile uses
a pinned Python image, installs only production dependencies, and runs as UID 10001.

## Live portal walkthrough

1. Open https://localhost:8443 and sign in with GitHub as `prasanthece42`.
2. Choose Register application, then Upload a new app. Select `hello-portal.zip`.
3. Inspect the final files and review the public destination `prasanthece42/hello-portal`.
4. Click Create repository and upload. Use Recover previous upload after an interruption.
5. Confirm application ID `hello-portal`, port `8000`, health `/health`, and resource `small`.
6. Review the proposed pipeline files. An authorized maintainer installs them separately;
   the portal does not have workflow-write permission.
7. Continue registration and submit the catalog proposal for maintainer review.
8. Complete DEV target setup and wait for a validated release. Select that release,
   review DEV, and confirm deployment through the existing signed request flow.

Uploading source does not create a catalog PR or deploy the application. Existing repositories
must be selected through the existing-repository path; upload recovery never recreates a repo.
