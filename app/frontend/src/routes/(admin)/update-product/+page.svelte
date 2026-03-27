<script>
	import { onMount } from 'svelte';
	import { toast } from 'svelte-sonner';
	import { page } from '$app/state';
	import { fetchProducts } from '$lib/api.js';
	import { invalidateProducts } from '$lib/products.svelte.js';

	let product = $state(null);
	let newProduct = $state({});
	// note: product and newProduct are $state so they stay reactive in runes mode
	let imagePreviews = $state({ image: '', image2: '', image3: '' });

	// Generic drop handler — writes base64 to newProduct[field] and updates preview
	function makeDropHandler(field) {
		return (e) => {
			e.preventDefault();
			const file = e.dataTransfer.files[0];
			if (!file) return;
			const reader = new FileReader();
			reader.onload = () => {
				imagePreviews[field] = reader.result;
				newProduct[field] = reader.result;
			};
			reader.readAsDataURL(file);
		};
	}

	const id = page.url.searchParams.get('id');

	onMount(async () => {
		const products = await fetchProducts();
		product = products.find((p) => p.id == id) ?? null;
		if (product) {
			newProduct = { ...product };
			imagePreviews.image  = product.image  ?? '';
			imagePreviews.image2 = product.image2 ?? '';
			imagePreviews.image3 = product.image3 ?? '';
		}
	});

	async function updateProduct() {
		const response = await fetch(`/api/products/${newProduct.id}`, {
			method: 'PUT',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(newProduct)
		});
		if (!response.ok) throw new Error(`HTTP ${response.status}`);
		return await response.json();
	}

	const placeholder = {
		name: 'str',
		size: 'str',
		brand: 'str',
		info: 'str',
		category: 'str',
		price: 'float',
		description: 'str'
	};

	const imageFields = [
		{ key: 'image',  label: 'Main image' },
		{ key: 'image2', label: 'Image 2' },
		{ key: 'image3', label: 'Image 3' },
	];
</script>

<a href="/product-list/" class="mt-4 inline-block px-6 text-gray-500 hover:text-gray-900">← Product List</a>
<h1 class="my-8 text-center text-3xl font-bold">Update Product with id: {product?.id}</h1>
<div class="mt-8 flex justify-center">
	<div class="flex flex-col gap-4">
		<!-- Dynamic text fields (excludes id, description, and image fields) -->
		{#each Object.keys(product ?? {}).filter((k) => !['id', 'description', 'image', 'image2', 'image3'].includes(k)) as key}
			<div class="flex gap-1">
				<label for={key} class="inline-block w-48 rounded bg-slate-600 px-4 py-2 text-right text-white">
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
						class="absolute top-2 left-3 text-sm text-gray-400 transition-all peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:bg-white peer-focus:px-1 peer-focus:text-xs peer-[:not(:placeholder-shown)]:-top-3 peer-[:not(:placeholder-shown)]:bg-white peer-[:not(:placeholder-shown)]:px-1 peer-[:not(:placeholder-shown)]:text-xs"
					>{placeholder[key]}</label>
				</div>
			</div>
		{/each}

		<!-- Image drop zones — shows current image above each drop zone -->
		{#each imageFields as { key, label }}
			<div class="flex gap-1">
				<label for="drop-{key}" class="inline-block w-48 rounded bg-slate-600 px-4 py-2 text-right text-white">
					{label}
				</label>
				<div class="flex flex-col gap-2">
					{#if imagePreviews[key]}
						<img src={imagePreviews[key]} alt="current" class="h-16 w-16 object-contain" />
					{:else}
						<span class="text-sm text-gray-400">no image</span>
					{/if}
					<div
						id="drop-{key}"
						class="flex w-72 items-center justify-center rounded border-2 border-dashed border-gray-400 px-4 py-4 text-sm text-gray-400 transition hover:border-gray-700"
						role="button"
						tabindex="0"
						ondrop={makeDropHandler(key)}
						ondragover={(e) => e.preventDefault()}
					>
						{imagePreviews[key] ? 'Drop to replace' : 'Drop image here'}
					</div>
				</div>
			</div>
		{/each}

		<!-- Description — HTML supported -->
		<div class="flex items-start gap-1">
			<label for="description" class="inline-block w-48 rounded bg-slate-600 px-4 py-2 text-right text-white">
				description
			</label>
			<div class="flex flex-col gap-1">
				<textarea
					id="description"
					bind:value={newProduct['description']}
					class="w-72 rounded border-2 border-gray-900 px-4 py-2 outline-none"
					autocomplete="off"
						rows="10"
					placeholder="HTML supported: <b>bold</b>, <ul><li>item</li></ul>"
				></textarea>
				<span class="text-xs text-gray-400">HTML: &lt;b&gt;, &lt;ul&gt;&lt;li&gt;, &lt;br&gt; …</span>
			</div>
		</div>

		<!-- Buttons -->
		<div class="mb-8 flex gap-4">
			<button
				class="rounded bg-slate-400 px-4 py-2 text-white transition hover:bg-gray-900"
				onclick={() => toast.error('canceled')}
			>cancel</button>
			<button
				class="ml-auto rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
				onclick={async () => {
					try {
						await updateProduct();
						invalidateProducts();
						toast.success('Product updated!');
					} catch {
						toast.error('Error!');
					}
				}}
			>save</button>
		</div>
	</div>
</div>
