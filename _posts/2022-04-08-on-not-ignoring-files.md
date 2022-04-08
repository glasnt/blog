---
title: On not ignoring files in Cloud Run deployments
---

With the new `gcloud run deploy --source` feature, it's a one-step process to both build your container and deploy it to a new service. 

But depending on what service that is, some things might get ignored. 

I ran into this today, trying out [Next.js](https://nextjs.org/) for the first time. In it's [deployment documentation](https://nextjs.org/docs/deployment), it says after running `next build` it will generate files in a `.next` folder. 

The problem is that hidden folders like this are automatically ignored by Cloud Build, and so they don't appear in the uploaded source code, and thus don't appear in your image!

You can get around this by using the `.gcloudignore` file to not exclude, but *explicitly include* files. 

```
echo "\!.next/" >> .gcloudignore
```

This command will create a file called `.gcloudignore` with the contents `!.next/`, which will ensure any folder called `.next` *is* uploaded when deploying. 

---

Bonus feature: yes I'm deploying JavaScript static sites to Cloud Run. I'm doing this by including a simple little `package.json` that will serve my files, and by having a `package.json` the service is detected as being Nodejs in Cloud Buildpacks and so it all works: 
```
{
  "scripts": {
    "start": "http-server"
  },
  "dependencies": {
    "http-server": "*"
  }
}
```
