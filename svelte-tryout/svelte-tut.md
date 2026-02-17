
[[https://svelte.dev/tutorial/svelte/welcome-to-svelte]]

> Motivation: Svelte : React ≈ Linux : Windows

# basics
**Svelte** = UI-Framework (wie React/Vue)

- Schreibst `.svelte` Komponenten mit HTML/CSS/JS
- Compiler wandelt das in effizientes Vanilla JS um
- staerke: haelt DOM in sync mit meiner app.  

**Vite** = Build-Tool & Dev-Server

- Startet schnellen Dev-Server mit Hot Module Replacement (Änderungen sofort sichtbar)
- Bundelt deine App für Production (optimiert, minified)
- Managed Assets (CSS, Bilder, etc.)

**svelte**  kompiliert in kleien effiziente js modules
**svelteKit** kann die ganze frontend app enthalten 

**component**: reusable self-contained block of code that encapsulates HTML, CSS and JavaScript
**runes** variablen, die gewrappt werden durch svelte (auch function())

# kompiliert zu vanilla js
> der output ist so als ob ich das mit grossem Aufwand selbst direkt in js geschrieben hätte ohne framework

# installation/ projekt erstellen
mit pacman muss ich nichts intallieren. ein neues projekt kann folgendermassen gestartet werden:
```zsh
# einziges requirement: npm muss istalliert sein. 
npm create vite@latest my-app -- --template svelte # ohne kit
```

```
# In das Projektverzeichnis wechseln
cd my-app  # App.svelte liegt hier

# Alle Abhängigkeiten installieren (SvelteKit, Vite, Svelte, etc.)
npm install  # kreiert in jedem projekt eine venv. (1st time only)

# Entwicklungsserver starten (läuft auf http://localhost:5173)
npm run dev -- --open  # -- open fakultativ, -- trennt argumente fuer npm/vite
=> --open geht an den server vite. # start in toblevel! (nicht scr wo App.velte liegt!)
```

```zsh
  Successfully installed dependencies with npm
│
◇  Successfully formatted modified files
│
◇  What's next? ────────────────────────╮
│                                       │
│  📁 Project steps                     │
│                                       │
│    1: cd my-app                       │
│    2: npm run dev -- --open           │
│                                       │
│  To close the dev server, hit Ctrl-C  │
│                                       │
│  Stuck? Visit us at                   │
│  https://svelte.dev/chat  ;
```
# spaeter fuer testing nur noch
```zsh
npm run dev # fuer testing - aenderungen im  laufenden system!
npm run build # fuer productionj
```

# bei groessernen aendewrungen
```zsh
npm install
```
wenn...
- Neue Dependencies hinzugefügt wurden
- Nach `git clone` eines bestehenden Projekts
- `node_modules/` Ordner gelöscht wurde
# typische projekt-struktur 
```text
~/projects/
├── my-python-project/
│   ├── venv/
│   ├── main.py
│   └── requirements.txt
└── my-svelte-app/
    ├── node_modules/
    ├── src/
	|	└── App.svelte # hier ist die main app 
    └── package.json
```

# ports
## vite-port  
  
```
   ➜  Local:   http://localhost:5173/
```
## documentation
```bash
.../docs # swagger
.../redoc # redoc
```

# modularisierung (nesting)

im script-tag in .svelte kann man weitere components importieren:
```js
<script>
	import Nested from './Nested.svelte';
</script>
```

das gegenstueck:
```js
<script>
	export const counter = 	...
```

das nested file uebern nimmt nicht den style aus main

# render variable text from files
```js
<@html string\>  /* file included. \excaping kann notwendig sein. gg
```

# declare variable for sync
```js
<script>
	let count = $state(0);

	function increment() {
		count += 1;
	}
</script>
```
tells svelte, that this is not an ordinary variable. state ist only reactive if there is  something that reacts on it. 

## Terminology
**Rune** 
Ein mystisches oder magisches Symbol, das in der nordischen Mythologie und germanischen Kultur oft mit Zaubersprüchen, Macht und verborgener Wirkung assoziiert wurde.
**Signal**
→ Der aktuell am häufigsten und korrektest verwendete Begriff in der Svelte-Community und in Vergleichen zu anderen Frameworks.
→ Betont: „Das ist ein reaktives Signal, das Änderungen sendet und empfängt.“
→ Aktiv & dynamisch.
**Reactive** **Signal**
→ Noch etwas genauer, wenn du den Kontext brauchst.

**(State)-Proxy** → sehr präzise für Objekte/Arrays („state proxy“, „deeply reactive state proxy“ in der offiziellen Svelte-Dokumentation)
**Rune** → der übergeordnete Begriff („$state rune“), aber nicht spezifisch für $state()
**Reactivity marker / Marker** → wie „magical symbol that instructs the compiler“ (Rich Harris selbst nennt Runes so)

# state 
svelt reacts to reassociations as well as to mutations
```js
let numbers = $state([1, 2, 3, 4]);  // numbers is now a reactive proxy

	function addNumber() {
		numbers.push(0)
	}
```

# derived 
```js
let total = $derived(numbers.reduce((t, n) => t + n, 0));
```
im gegensatz zu state wird hier nicht neu zugeortned sondern updated, wenn die **dependency** updatet. 

# create a non reactive snapshot (for log())
```js
function addNumber() {
		numbers.push(numbers.length + 1);
		console.log($state.snapshot(numbers));
	}
	// alternative: when ever new snapshot ist generated $inspect(numbers)
	// or even $inspect(numbers).with(console.trace) -> see origin
```

bei
```js 
$inspect(nummbers).with(console.trace) entstehen in der console viele meta infos
```

# effect
```js
$effect(  /* ← hier kommt eine Funktion hin */  )
```
Aha eigentlich ändern sich die Argumente der von svelte gewrappten fkt das ist der trigger
## kurzschreibweise
```js
$effect( () => { ... } ) // ← das ist die gängige Kurzschreibweise
// ist dasselbe wie
function meinEffect() { setInterval(...); }

$effect(meinEffect);
```

## tut-ex
```js
$effect(() => {
		setInterval(() => {  // ruft in fixem zeitabstand auf. 
			eapsed += 1;
		}, interval);
	});

```

```js
setInterval(callback, time) // callback: fun, time z.b. 1000=1s
```

effect wird einmal  im dom gestartet, also die iteration ist nur durch die genestete fkt im gange. effect startet nur und was dann innerhalb der funtion passiert ist eine andere geschichte.

# universal reactivity
die datei shared.js funktioniert nicht, sie muss shared.svelte.js heissen, damit sie funktioniert
die datei Counter.svelte wird in App.svelte importiert und Counter wird als <Counter/> genutzt. das ist ein custom component. sie ist unsichtbar. die syntax ist svelte-spezifisch.

# interface zum ORM
```js
// FALSCH:
let data = $state(db.query());  // ❌

// RICHTIG:
let data = $state(null);  // ✅ Container parent
data = await db.query();  // ✅ Zuweisung = reactive
```

man kann nicht direkt die db.querry mit $ state beobachtjn man watched den container und 
svelte faengt die zuweisung ab. genial!

# effect, derived, State
# Svelte 5 Runes – Vergleich: $state • $derived • $effect

## Kurzfassung (Tabelle)

| Rune       | Zweck                             | Wer setzt den Wert?   | Kann man zuweisen? | Typischer Anwendungsfall                              | Side-Effects erlaubt?      | Rechnet neu bei …          | Lazy / Memoized?   |
| ---------- | --------------------------------- | --------------------- | ------------------ | ----------------------------------------------------- | -------------------------- | -------------------------- | ------------------ |
| `$state`   | Reaktiver **State** (Grundwert)   | Du selbst (User/Code) | Ja                 | Input-Werte, Listen, Zähler, geladene Daten           | Ja (aber besser vermeiden) | –                          | –                  |
| `$derived` | **Abgeleiteter Wert** (berechnet) | Svelte automatisch    | Nein (read-only)   | Filter, Sort, Summe, Formatierung, abgeleitete Listen | Nein (Fehler!)             | Abhängigkeiten ändern sich | Ja                 |
| `$effect`  | **Nebenwirkung** (Side-Effect)    | Svelte automatisch    | – (kein Wert)      | Logging, API-Calls, DOM-Manipulation, Subscriptions   | Ja (genau dafür da)        | Abhängigkeiten ändern sich | Nein (läuft immer) |

## Wann welches Rune nehmen? (Entscheidungsbaum)
>
>1. Ist es ein **Wert, den der User oder dein Code aktiv ändert**?  
   → **$state**

2. Ist es ein **Wert, der automatisch aus anderen Werten berechnet werden soll** (ohne Side-Effects)?  
   → **$derived**  
   (Filter, Sort, Summe, Formatierung, abgeleitete Listen, …)

3. Willst du bei Änderung von etwas **eine Aktion ausführen** (nicht nur berechnen)?  
   → **$effect**  
   (console.log, fetch, localStorage schreiben, DOM außerhalb von Svelte, …)

# logic
## general
syntax: starte mit $ ist in {}
**start**: {#logic}
**end**: {/logic}
**continue block**: {:logic}
## if
```js
<button onclick={increment}> // {} svelte spexifisch entspricht "increment"
```

```js
<script>
	let count = $state(0);

	function increment() {
		count += 1;
	}
</script>

<button onclick={increment}>
		Clicked {count}   // normalerweise kann man in html keine variabeln direkt integrieren!
	{count === 1 ? 'time' : 'times'}
</button>
```