---
title: Generative epiphany
---

I've recently been learning more about Generative AI and LLMs as part of my day job, and was having problems understanding some of the concepts. Evals, fine tuning, etc; it was all confusing to me.

Until I had an epiphany, and realised that I already have a mental model for this sort thing already: **containers**.

Dockerfiles that build containers are [just instructions](https://www.youtube.com/watch?v=tGseJW_uBB8) to build a tarball. That container image without the instructions is a black box. That black box could be an LLM Model.

*Prompt engineering* is changing the entrypoint of a LLM model.

*Fine Tuning* is adding more to layers into the container, by adding to the Dockerfile, adding onto the existing base container.

*Evaluation* is comparing the outputs of two different containers with custom args, or different base images.

*Retrieval Augmented Generation (RAG)* is connecting to a database. That could be a SQLite flatfile to add into the container, or it could be a live SQL database, information that is not baked into the model/container.

*Functions* are just functions, connecting to APIs.

*HuggingFace* is just Docker Hub, or any other hosting platform for blobs of stuff that you can call down by name.

You can also skip the whole Dockerfile part and use named models from a hosting provider, sort of like using Cloud Functions or Buildpacks for named programming environments. E.g. `gemini-1.5.-pro` is just contents of the `.python-version` file.

You will never see the contents of the Dockerfile, unless you build it yourself (and you may not need to, depending on your use case, you don't have to start `FROM scratch`).

*Note: this blogpost is more for me than anyone else, but please let me know if this helped map the concepts in your mind!*
