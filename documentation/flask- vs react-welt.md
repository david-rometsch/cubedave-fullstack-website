| Aspekt                         | Flask / Jinja (klassisch)                                   | React / SPA (moderne Client-seitige App)                           |
| ------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------ |
| Primäre Antwort an den Browser | fertiges HTML (Server hat schon gerendert)                  | kleines HTML-Gerüst + großes JavaScript-Bundle                     |
| Rendering-Ort                  | **Server** (Server-Side Rendering)                          | **Browser** (Client-Side Rendering)                                |
| Template-Syntax                | Jinja2 → `{{ variable }}`, `{% for %}` usw. im `.html`-File | JSX → `{variable}`, `{liste.map(...)}` direkt im JavaScript-Code   |
| Daten → Template               | Server füllt Daten in Template ein → fertiges HTML ans FE   | React-Komponente rendert im Browser → Daten per API nachgeladen    |
| Datenabruf                     | meist beim ersten Request (oder bei Form-POST / Redirect)   | meist nach dem Laden (useEffect, SWR, TanStack Query, …)           |
| Navigation / Seitenwechsel     | voller Page Reload → neuer Request an Server                | meist kein Reload → React Router wechselt Komponente client-seitig |
| Interaktivität                 | begrenzt (braucht meist Neuladen oder htmx/Alpine.js)       | vollständig client-seitig (State, Hooks, Events, Re-Render)        |
| Erster Byte Time (Performance) | schneller (fertiges HTML sofort)                            | langsamerer Start (JS muss erst laden & ausführen)                 |
| SEO ohne Extra-Arbeit          | sehr gut                                                    | schlecht bis mittel (braucht SSR/SSG/Prerendering)                 |
| Typische Datei-Endung          | `.html` + `.jinja`                                          | `.jsx` / `.tsx`                                                    |
| State-Management               | meist serverseitig (Session, DB, Redirects)                 | client-seitig (useState, useReducer, Zustand, Redux, …)            |
**Deine Flask-Analogie (sehr treffend):**

> Flask: info → jinja → template → schicken ans FE → Server ist der Renderer + Datenquelle + Template-Engine in einem → Der Browser bekommt ein fertiges Bild (HTML)

**Deine React-Analogie (auch sehr gut):**

> React: script (inkl template) schicken → React baut aus JS template und ruft apis auf → via api call wird das template auf dem FE ausgefüllt (gerendert)

**Noch etwas präziser formuliert:**

- **Flask/Jinja-Welt** Server → rendert Template mit Daten → schickt fertiges HTML → Browser zeigt es an
- **React-Welt** (klassisches CSR) Server → schickt leeres HTML + JS-Bundle (inkl. Komponenten/„Templates“ in JSX) → Browser → lädt JS → führt React aus → React-Komponenten rendern sich selbst → holen Daten per API → updaten den DOM dynamisch

**Kleiner Zusatz – die Hybrid-Welten (2025/2026 sehr relevant):**

- **Next.js App Router / Server Components** → sehr nah an Flask/Jinja: Server rendert Teile des HTML vorab → schickt fertiges HTML + JS → React „hydriert“ es nur noch
- **Remix / SolidStart / Astro** → versuchen ebenfalls, das Beste aus beiden Welten zu kombinieren (Server-Rendering + Islands-Architektur)