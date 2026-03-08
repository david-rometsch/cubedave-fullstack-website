<script>
	let cubeType = $state([]);
	let cubes = $state([]); // gets tracked now
	let cubeData = $state({});

	// fetch cubes from BE
	// async function getAllCubes() {
	// 	let responseJson = '';
	// 	try {
	// 		let response = await fetch('http://127.0.0.1:8000/api/all_cubes');
	// 		if (!response.ok) throw new Error(`HTTP Fehler! Status: ${response.status}`);
	// 		responseJson = await response.json();
	// 		cubes = responseJson.cubes;
	// 		cubes = JSON.stringify(responseJson, null, 2);
	// 		console.log('cubes: ', cubes); // output.textContent = JSON.stringify(data, null, 2)
	// 	} catch (err) {
	// 		// output.textContent = "Fehler: " + err.message
	// 		console.error('Fetch-Fehler:', err);
	// 	}
	// }
	// getAllCubes();

	const filteredCubes = $derived(cubes.filter((cube) => cube.category == cubeType));
</script>

<h1 class="my-8 text-center text-3xl font-bold">Welcome to my cubing site!</h1>

<div class="mx-auto max-w-3xl px-4 leading-relaxed text-gray-700">
	<p class="mb-4">This is just a preview, a lot of things aren't implemented yet.</p>
	<p>
		This site is done with Svelte. Visit
		<a
			href="https://svelte.dev/docs/kit"
			class="text-blue-600 hover:underline"
			target="_blank"
			rel="noopener noreferrer"
		>
			svelte.dev/docs/kit
		</a>
		to read the documentation.
	</p>
</div>
