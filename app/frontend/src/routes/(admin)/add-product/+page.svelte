<script>
	import { onMount } from 'svelte';
	import { toast } from 'svelte-sonner';
	import { fetchProducts } from '$lib/api.js';

	let products = [];
	let newProduct = {};
	let imagePreview = '';

	// Convert dropped image file to base64 data URL and store it in newProduct
	function handleDrop(e) {
		e.preventDefault();
		const file = e.dataTransfer.files[0];
		if (!file) return;
		const reader = new FileReader();
		reader.onload = () => {
			imagePreview = reader.result;
			newProduct.image = reader.result;
		};
		reader.readAsDataURL(file);
	}

	// Load one existing product to derive the field list dynamically
	onMount(async () => {
		products = await fetchProducts();
	});

	// Placeholder type hints shown in each input field
	const placeholder = {
		name: 'str',
		size: 'str',
		brand: 'str',
		info: 'str',
		category: 'str',
		price: 'float',
		image: 'str',
		description: 'str'
	};
</script>

<h1 class="my-8 text-center text-3xl font-bold">Add product</h1>
<div class="mt-8 flex justify-center">
	<div class="flex flex-col gap-4">
		<!-- Input rows — generated from the first product's keys, excluding handled fields -->
		{#each Object.keys(products[0] ?? {}).filter((k) => k !== 'description' && k !== 'id' && k !== 'image') as key}
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
					<!-- Floating label acting as type hint -->
					<label
						for={key}
						class="absolute top-2 left-3 text-sm text-gray-400 transition-all peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:bg-white peer-focus:px-1 peer-focus:text-xs"
						>{placeholder[key]}
					</label>
				</div>
			</div>
		{/each}

		<!-- Image drag & drop -->
		<div class="flex gap-1">
			<label for="image-drop" class="inline-block w-48 rounded bg-slate-600 px-4 py-2 text-right text-white">
				image
			</label>
			<div
				id="image-drop"
				class="flex w-72 items-center justify-center rounded border-2 border-dashed border-gray-400 px-4 py-4 text-sm text-gray-400 transition hover:border-gray-700"
				role="button"
				tabindex="0"
				ondrop={handleDrop}
				ondragover={(e) => e.preventDefault()}
			>
				{#if imagePreview}
					<img src={imagePreview} alt="preview" class="max-h-24 object-contain" />
				{:else}
					Bild hier ablegen
				{/if}
			</div>
		</div>

		<!-- Description in a larger textarea -->
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
				>textarea</textarea
			>
		</div>

		<!-- buttons -->
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
				}}>add</button
			>
		</div>
	</div>
</div>
