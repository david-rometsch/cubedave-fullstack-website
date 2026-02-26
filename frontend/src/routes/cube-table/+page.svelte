<script>
	import { cubeData } from './cubes.svelte.js';
	let cubes = $state(cubeData.cubes); // gets tracked now
	let cubeType = $state('');
	// const filteredCubes = $derived(cubes.filter((cube) => cube.category == cubeType));
	const filteredCubes = $derived((cubes ?? []).filter((cube) => cube.category == cubeType));

	// fetch cubes from BE
	async function getAllCubes() {
		let responseJson = '';
		try {
			let response = await fetch('http://127.0.0.1:8000/api/all_cubes');
			if (!response.ok) throw new Error(`HTTP Fehler! Status: ${response.status}`);
			responseJson = await response.json();
			cubes = responseJson;
			// cubes = JSON.stringify(responseJson, null, 2);
			// console.log('cubes: ', cubes); // output.textContent = JSON.stringify(data, null, 2)
		} catch (err) {
			// output.textContent = "Fehler: " + err.message
			console.error('Fetch-Fehler:', err);
		}
		// console.log("response: ", responseJson);
		// cubeData = responseJson;
	}
	getAllCubes();
</script>

<!-- <script> -->
<!-- 	let { children } = $props(); -->
<!-- </script> -->

<h1>Welcome to the cube-table-page !</h1>

<h1>Cubes aus JSON</h1>

<!-- <p>{JSON.stringify(cubes, null, 2)}</p> -->
<!-- filter -->
<div class="mt-4 flex gap-3">
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			cubeType = '3x3';
		}}
	>
		3x3
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			cubeType = '4x4';
		}}
	>
		4x4
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			cubeType = '2x2';
		}}
	>
		2x2
	</button>
</div>

<!-- Tabelle -->
<table b <table class="mt-6 w-full border-collapse">
	<thead class="bg-gray-800 text-white">
		<tr>
			<th class="px-4 py-2 text-left">Name</th>
			<th class="px-4 py-2 text-left">Size</th>
		</tr>
	</thead>
	<tbody>
		{#each filteredCubes as cube}
			<tr class="border-b border-gray-200 hover:bg-gray-100">
				<td class="px-4 py-2">{cube.name}</td>
				<td class="px-4 py-2">{cube.size}</td>
			</tr>
		{/each}
	</tbody>
</table>
