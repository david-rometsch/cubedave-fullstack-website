<script>
	import { TwistyPlayer } from 'cubing/twisty';
	import { Alg } from 'cubing/alg';

	let open = $state({});
	const toggle = (i) => (open[i] = !open[i]);

	let videoReady = $state(false);
	let videoEl = $state(null);

	function onCanPlayThrough() {
		videoReady = true;
	}

	// Use 'arrow' as a placeholder — the template renders it as an inline SVG
	const sections = [
		{
			title: 'Basic Motion',
			headerImages: [],
			content: `<p>Use the animation on the right side to learn the for moves of the basic motion. <ul>Tipps<li>Go step by step with the arrow towards right</li><li>set it back to start with the double arrow to the left</li></p>`,
			aside: `<twisty-player
  puzzle="3x3x3"
	alg="R U R' U'"
  visualization="3D"
  background="none"
  control-panel="bottom-row"
	anchor="start"
  style="width:100%;height:300px"
></twisty-player>`
		},
		{
			title: 'Fingertricks',
			headerImages: [],
			content: `<p>Here again the basic motion. Watch precisley how to use your fingers.<br>Do it 6 times and the cube is solved again!<br>Can you do it in under 3 seconds? It's possible!<br><a href="product/10">Get the official Speedcubing Timer here.</a></p>`,
			video: '/images/grundbewegung-mute.mp4'
		},
		{
			title: 'Step 1 — Fake Cross',
			headerImages: ['/images/step1/1.png', 'arrow', '/images/step1/3.png'],
			content: `<p>Describe how to solve the cross here.</p>
<ul>
  <li>Tip one</li>
  <li>Tip two</li>
</ul>`,
			aside: null
		},
		{
			title: 'Step 2 — Real Cross',
			headerImages: ['/images/step2/1.png', 'arrow', '/images/step2/3.png'],
			content: `<p>Describe how to insert the first-layer corners.</p>`,
			aside: null
		},
		{
			title: 'Step 3 — First Layer Corners',
			headerImages: ['/images/step3/1.png', 'arrow', '/images/step3/3.png'],
			content: `<p>Describe how to place the second-layer edges.</p>`,
			aside: null
		}
	];
</script>

<h1 class="my-8 text-center text-3xl font-bold">Learn how to Be Fast!</h1>

<div class="mx-auto max-w-4xl px-6 pb-16">
	{#each sections as section, i}
		<div class="mb-3 overflow-hidden rounded border border-gray-200">
			<!-- Accordion header: 3-column grid so images are always truly centered -->
			<button
				class="grid w-full grid-cols-[1fr_auto_1fr] items-center bg-gray-800 px-5 py-3 text-white transition hover:bg-gray-700"
				onclick={() => toggle(i)}
			>
				<!-- Col 1: title (left-aligned) -->
				<span class="text-left text-base font-semibold">{section.title}</span>

				<!-- Col 2: header images (true center) -->
				<div class="flex items-center gap-3">
					{#each section.headerImages as img}
						{#if img === 'arrow'}
							<!-- Generated SVG arrow — rounded chevron pointing right -->
							<svg viewBox="0 0 48 32" class="h-8 w-12 shrink-0" xmlns="http://www.w3.org/2000/svg">
								<!-- Shaft + arrowhead as one filled shape, rounded everywhere -->
								<path
									d="M2 11 L28 11 L28 4 Q28 2 30 3.5 L46 15 Q48 16 46 17.5 L30 28.5 Q28 30 28 28 L28 21 L2 21 Q0 21 0 19 L0 13 Q0 11 2 11 Z"
									fill="white"
									rx="3"
								/>
							</svg>
						{:else}
							<img src={img} alt="" class="h-12 w-12 rounded bg-slate-100 object-contain p-0.5" />
						{/if}
					{/each}
				</div>

				<!-- Col 3: toggle symbol (right-aligned) -->
				<span class="text-right text-xl leading-none">{open[i] ? '−' : '+'}</span>
			</button>

			<!-- Accordion body -->
			{#if open[i]}
				<div class="flex gap-8 p-6">
					<!-- Left / full: text content -->
					<div class="prose flex-1 text-gray-700">
						{@html section.content}
					</div>

					<!-- Right: free aside slot — mp4, img, iframe, animation, anything -->
					{#if section.video}
						<div class="relative w-80 shrink-0">
							{#if !videoReady}
								<div class="absolute inset-0 flex items-center justify-center bg-black/10 rounded">
									<div class="h-10 w-10 animate-spin rounded-full border-4 border-gray-300 border-t-blue-600"></div>
								</div>
							{/if}
							<video
								bind:this={videoEl}
								src={section.video}
								controls
								preload="auto"
								class="w-full rounded"
								style={videoReady ? '' : 'visibility: hidden;'}
								oncanplaythrough={onCanPlayThrough}
							></video>
						</div>
					{:else if section.aside}
						<div class="w-80 shrink-0">
							{@html section.aside}
						</div>
					{/if}
				</div>
			{/if}
		</div>
	{/each}
</div>
