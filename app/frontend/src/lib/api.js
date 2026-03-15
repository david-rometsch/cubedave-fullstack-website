export async function fetchProducts() {
	const res = await fetch('/api/all_product');
	if (!res.ok) throw new Error(`HTTP ${res.status}`);
	return res.json();
}
