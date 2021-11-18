# Knowledge Share - Kubernetes Health Checks

## Neat-o script:
* what are healthchecks for?
    * it's kind-of like poking roadkill with a stick.  "Hey, are you alive?"
    * (usually) should be inexpensive/fast
* 3 subtypes of healthchecks
    * [startup](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-startup-probes)
    * [liveness](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-http-request)
    * [readiness](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes)
* what is a [probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes)
* 3 subtypes of probes
    * [HTTP](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#http-probes)
    * [TCP](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#tcp-probes)
    * [exec]()
    
* live demo
* gotchas
    * multiple probes at once don't wait for one another
    * "exec true" is a nightmare
    * probes are a _container_-centric idea, not _pod_

## Have some more time?  Here are some good links
* [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) - official Kubernetes docs
* [Understanding Kubernetes Probes](https://blog.devgenius.io/understanding-kubernetes-probes-5daaff67599a) - blog post by Yitaek Hwang