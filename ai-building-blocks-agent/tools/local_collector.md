# Spinup Local OTEL Collector

```bash
docker run -p 4317:4317 -p 16686:16686 \
       --name jaeger \
       jaegertracing/all-in-one:1.57
```

Open [http://localhost:16686](http://localhost:16686) to browse traces

---

## Managing the Jaeger Container

**See all containers (running or stopped):**

```bash
docker ps -a
```

You’ll see the “jaeger” container listed with an EXITED status.

**Remove the old “jaeger” container (so you can re-use that name):**

```bash
docker rm jaeger
```

**Re-run your Jaeger container:**

```bash
docker run -p 4317:4317 -p 16686:16686 \
    --name jaeger \
    jaegertracing/all-in-one:1.57
```

**Verify it’s running:**

```bash
docker ps
```

You should now see “jaeger” in the list with its ports mapped.

**Alternatively**, to start the stopped container instead of recreating it:

```bash
docker start jaeger
docker ps
```
