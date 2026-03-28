<script>
	import { nav } from '$lib/nav.svelte.js';

	const backUrl = nav.prev;
	const backLabel = backUrl?.match(/^\/product\/\d+/) ? '← Back to Product' : '← Back';
</script>

<h1 class="my-8 text-center text-3xl font-bold">CubeDave's Cube Knowledge</h1>

{#if backUrl}
	<a href={backUrl} class="mt-4 inline-block px-6 text-gray-500 hover:text-gray-900">{backLabel}</a>
{/if}

<div class="mx-auto max-w-prose">
	<h2 id="magnetic" class="text-center text-xl font-bold">Magnetic vs. Non-Magnetic</h2>
	<p class="text-justify text-base">
		Nowadays most speedcubes have magnets. These magnets help you align the layers. Cubes
		with magnets are only slightly more expensive, so I would give a clear recommendation to buy a
		cube with magnets, even if you are a beginner.
	</p>
	<hr class="my-8 border-gray-300" />
	<h2 id="cornercutting" class="text-center text-xl font-bold">Cornercutting</h2>
	<p class="text-justify text-base">
		Cornercutting is the amount of misalignment the cube can tolerate and still perform the move you
		intended.
	</p>
	<ul>
		<li>
			Forward cornercutting (or just cornercutting): here you test to what degree of
			misalignment the layer will still complete its move.
		</li>
		<li>
			Reverse cornercutting: here you test at what degree of misalignment the layer will snap back
			into the old position.
		</li>
	</ul>
	<hr class="my-8 border-gray-300" />
	<h2 id="maglev" class="text-center text-xl font-bold">MagLev</h2>
	<p class="text-justify text-base">
		MagLev is an upgrade over springs on the center pieces. It reduces friction and noise. Two
		repelling ring-shaped magnets are implemented to achieve smoother cushioning.
	</p>
	<hr class="my-8 border-gray-300" />
	<h2 id="uv" class="text-center text-xl font-bold">UV-Coating</h2>
	<p class="text-justify text-base">
		UV-Coating improves the grip on the cube. A thin extra layer of UV-coating is applied on the
		surface of the cube.
	</p>
</div>
