---
title: Meridian
type: landing
date: 2024-01-01

design:
  spacing: '5rem'

sections:
  - block: markdown
    content:
      title: Financial Technology Advisory
      subtitle: Ayudo a dueños de empresas familiares con ambiciones globales a planificar un legado financiero con absoluta claridad.
      text: |
        16 años en la intersección de tecnología y banca institucional. Con diplomados en alta tecnología aplicada al sector financiero, convierto el laberinto de regulaciones en una estrategia que puedes ejecutar.

        [Agenda una conversación](https://cal.com/elidiazgt/30min)

  - block: collection
    id: recent-posts
    content:
      title: Latest Insights
      filters:
        folders:
          - blog
      limit: 3
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: recent-posts-es
    content:
      title: Artículos en Español
      filters:
        folders:
          - blog/es
      limit: 3
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: events
    content:
      title: Events
      filters:
        folders:
          - events
      limit: 2
    design:
      view: compact
---