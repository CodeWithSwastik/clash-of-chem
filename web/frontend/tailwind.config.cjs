/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				'dark': "#191816",
				'fg-dark': "#22231f",
			}
		}
	},
	plugins: []
};
