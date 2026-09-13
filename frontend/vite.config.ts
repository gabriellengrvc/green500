import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import tailwindcss from "@tailwindcss/vite"

export default defineConfig({
  plugins: [react(), tailwindcss()],
  base: "/static/dashboard/",
  build: {
    outDir: "../green500/static/dashboard",
    emptyOutDir: true,
  },
})
