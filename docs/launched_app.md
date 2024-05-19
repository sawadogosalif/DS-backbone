

# Exécution d'une application dans un conteneur Docker et accès depuis votre navigateur

Les conteneurs Docker offrent une manière pratique d'exécuter des applications de manière isolée et portable. Lorsque vous exécutez une application dans un conteneur Docker, vous pouvez l'exposer sur un port spécifique de votre système hôte pour y accéder depuis un navigateur Web.

Dans ce tutoriel, nous allons vous montrer comment exécuter une application dans un conteneur Docker et y accéder à partir de votre navigateur en utilisant un exemple concret.

## Étape 1 : Exécution de l'application dans un conteneur Docker

Pour commencer, vous devez avoir Docker installé sur votre système. Une fois Docker installé, vous pouvez exécuter l'application dans un conteneur Docker en utilisant la commande `docker run`.

Supposons que vous ayez une application nommée "dash" que vous souhaitez exécuter dans un conteneur Docker. Vous pouvez utiliser la commande suivante pour démarrer le conteneur :

```bash
docker run -p 8050:9000 dash
```

Dans cette commande :

- `docker run` est la commande utilisée pour démarrer un conteneur Docker.
- `-p 8050:9000` spécifie que le port 9000 de votre conteneur Docker sera exposé sur le port 8050 de votre système hôte. Cela signifie que toute communication entrante sur le port 8050 de votre système hôte sera redirigée vers le port 9000 du conteneur Docker.
- `dash` est le nom de l'image Docker à partir de laquelle le conteneur sera créé.

## Étape 2 : Accès à l'application depuis votre navigateur

Une fois que le conteneur Docker est en cours d'exécution, vous pouvez accéder à votre application à partir de votre navigateur Web en utilisant l'URL suivante :

```
http://localhost:8050
```

En utilisant cette URL, votre navigateur enverra une requête au port 8050 de votre système hôte, qui sera redirigée vers le port 9000 du conteneur Docker où votre application est en cours d'exécution.

Assurez-vous simplement que votre application est configurée pour écouter sur le port 9000 à l'intérieur du conteneur Docker, car c'est le port qui est exposé à votre système hôte.

