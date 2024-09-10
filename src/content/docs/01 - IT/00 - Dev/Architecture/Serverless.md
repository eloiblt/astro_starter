---
title: "Serverless"
---

## Introduction

There is a server ! 
But developers don't have to manage deployments / pipelines / infrastructure. They only focus on code.

Le code doit être décomposé en fonctions, qui ont un unique but (Functions As A Service). 

Scaling automatique + only pay for what you use (millisecondes comme unité de paiement)

Les fonctions peut écouter / déclencher des évènements, pour déclencer des fonctions. Ex : à chaque enregistrement dans une bd. 

## Fournisseurs

Différentes compatibilité langage. 

AWS Lambda
Azure Function
Google Cloud Functions
Vercel 
Netlify
## Practical

Avec AWS, on crée un projet avec leur CLI, et on a un fichier `template.yaml`, qui définie toutes les fonctions de l'applications, leur emplacement et leur language. Après déploiement, on les appelle en HTTP.

## Vs Microservices

Les microservices sont généralement + gros que les fonctions serverless. 
Une fonction serverless c'est un point d'entrée, un tout petit traitement. 
## Pros

No server maintenance
Low cost
Easy to scale
Strong dependance to cloud provider

## Cons

Cold start
No filesystem
