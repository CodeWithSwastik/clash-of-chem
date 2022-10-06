/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	darkMode: true,
	theme: {
<<<<<<< HEAD
=======
		extend: {
			colors: {
				dark: '#191816',
				'fg-dark': '#22231f'
			},
			animation: {
				'spin-slow': 'spin 2s linear infinite'
			}
		}
>>>>>>> b54a6ead9cad6798fc46a47b04139e4b886b9e62
	},
	plugins: [require('@catppuccin/tailwindcss')]
};
