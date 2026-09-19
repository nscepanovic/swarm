import path from "node:path";
import { fileURLToPath } from "node:url";

/** @type {import('next').NextConfig} */
export default {
  poweredByHeader: false,
  reactStrictMode: true,
  // aplikacija je samostalna u swarm/app; ne gledaj lockfile-ove iznad
  turbopack: { root: path.dirname(fileURLToPath(import.meta.url)) },
};
