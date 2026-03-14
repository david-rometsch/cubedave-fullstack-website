// fetch product from BE export async function getAllproduct() {
let responseJson = '';
try {
	let response = await fetch('/api/all_product');
	if (!response.ok) throw new Error(`HTTP Fehler! Status: ${response.status}`);
	responseJson = await response.json();
	// console.log(`product: ${product}`);
	console.log(`response json: ${responseJson}`);
	product = responseJson;
} catch (err) {
	// output.textContent = "Fehler: " + err.message
	// console.error('Fetch-Fehler:', err);
}
