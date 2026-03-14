<script>
	import { onMount } from 'svelte';
	import { toast } from 'svelte-sonner';
	import { marked } from 'marked';

	let products = [];
	let fields = [];
	let newProduct = {};
	let image = '';
	// fetch product-fields dynamically
	onMount(() => {
		async function getAllproduct() {
			let responseJson = '';
			try {
				let response = await fetch('/api/all_product');
				if (!response.ok) throw new Error(`HTTP Fehler! Status: ${response.status}`);
				responseJson = await response.json();
				products = responseJson;
				console.log(products);
				// console.log(product);
			} catch (err) {
				// output.textContent = "Fehler: " + err.message
				console.error('Fetch-Fehler:', err);
			}
		}
		getAllproduct();
	});
	//prepare placeholderf vor each field
	const placeholder = {
		name: 'str',
		size: 'str',
		brand: 'str',
		magnetic: 'str',
		category: 'str',
		image: 'str',
		description: 'str'
	};
</script>

<h1 class="my-8 text-center text-3xl font-bold">Add product</h1>
<div class="mt-8 flex justify-center">
	<div class="flex flex-col gap-4">
		<!-- rows -->
		{#each Object.keys(products[0] ?? {}).filter((k) => k !== 'description') as key}
			<div class="flex gap-1">
				<label
					for="name"
					class=" w- inline-block w-48 rounded bg-slate-600 px-4 py-2 text-right text-white"
				>
					{key}
				</label>

				<div class="relative">
					<input
						id={key}
						autocomplete="off"
						type="text"
						bind:value={newProduct[key]}
						class="peer w-72 rounded border-2 border-gray-900 px-4 py-2 outline-none"
						placeholder=" "
					/>
					<label
						for={key}
						class="absolute top-2 left-3 text-sm text-gray-400 transition-all peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:bg-white peer-focus:px-1 peer-focus:text-xs"
						>{placeholder[key]}
					</label>
				</div>
			</div>
		{/each}
		<!-- different for image -->
		<div>
			<label
				for="name"
				class="inline-block w-48 rounded bg-slate-600 px-4 py-2 text-right text-white"
			>
				image
			</label>
			<input
				autocomplete="off"
				type="text"
				id="name"
				name="name"
				required
				minlength="4"
				maxlength="8"
				size="10"
				bind:value={image}
				class="w-72 rounded border-2 border-gray-900 px-4 py-2 outline-none"
			/>
		</div>
		<!-- long description-text in bigger box -->
		<div class="gap- flex items-start gap-1">
			<label
				for="name"
				class="inline-block w-48 rounded bg-slate-600 px-4 py-2 text-right text-white"
				>description
			</label>
			<textarea
				bind:value={newProduct['description']}
				class="w-72 rounded border-2 border-gray-900 px-4 py-2 outline-none"
				autocomplete="off"
				type="text"
				id="name"
				name="name"
				required
				maxlength="250"
				rows="10"
				oninput={() => console.log(newProduct['description'])}
				onkeydown={(e) => e.key === 'Enter' && console.log(newProduct['description'])}
				>textarea</textarea
			>
		</div>

		<!-- Buttons  -->
		<div class="mb-8 flex gap-4">
			<button
				class="rounded bg-slate-400 px-4 py-2 text-white transition hover:bg-gray-900 hover:bg-slate-400"
				onclick={() => {
					toast.error('canceled');
				}}>cancel</button
			>
			<button
				class="ml-auto justify-end gap-4 rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
				onclick={async () => {
					const response = await fetch('/api/add_product', {
						method: 'POST',
						headers: { 'Content-Type': 'application/json' },
						body: JSON.stringify(newProduct)
					});
					if (response.ok) toast.success('Product added!');
					else toast.error('Error!');
					console.log(newProduct);
				}}>add</button
			>
		</div>
	</div>
</div>
