---
title: "Modular monolith"
---

Architecture that combines :
- the **benefits of modular design** (like microservices)
- with the **simplicity** of a **monolithic** architecture. 
## Introduction

It involves dividing the system into a set of **loosely-coupled modules**, each with a well-defined boundary and explicit dependencies on other modules.

We **still build and deploy a single application** which is same with **traditional Monolith architecture**, but we build application with **breaking up the code into independent modules** for each of the features needed in our application.

Maximum de séparation : chaque module à son schéma en BD, un module n'écrit pas dans les tables de son voisin, mais il appelle ses API (pas HTTP, sa fonction). 

## Comparaison avec les microservices 

![](https://i.postimg.cc/BvtK1qDn/d8ace7e6-f35c-4d0b-b898-9adf626ef647.webp)

Vs Microservices : 

![test](https://i.postimg.cc/k4bRffTr/820d97ec-69cb-47b2-87f7-60b28be8a660.webp)

## Pros (vs microservices)

- High reusability of code 
- Easy to refactor
- Better organized dependencies
- Less complex than microservices architecture
- Better for teams
- Possible to migrate to microservices later

## Cons

- Can't diversify technology
- Can't scale and deploy independently
