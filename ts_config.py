{
  "compilerOptions": {
    "target": "ES2020",                  // Compile TS to ES2020 JavaScript
    "useDefineForClassFields": true,     // Use `define` semantics for class fields
    "lib": ["ES2020", "DOM", "DOM.Iterable"], // Include standard libraries
    "module": "ESNext",                  // Use ES module syntax for output
    "skipLibCheck": true,                // Skip type checking of declaration files

    /* Bundler mode */
    "moduleResolution": "bundler",       // Optimized resolution for bundlers like Vite
    "allowImportingTsExtensions": true,  // Allow imports with .ts / .tsx extensions
    "isolatedModules": true,             // Each file is treated as a module (for bundlers)
    "moduleDetection": "force",          // Force TS to detect modules
    "noEmit": true,                      // Do not output compiled JS (used for type-checking only)
    "jsx": "react-jsx",                  // Use the new JSX transform

    /* Strict linting and code quality */
    "strict": true,                      // Enable all strict type checks
    "noUnusedLocals": true,              // Error on unused local variables
    "noUnusedParameters": true,          // Error on unused function parameters
    "noFallthroughCasesInSwitch": true   // Error on switch fallthrough
  },
  "include": ["src"]                      // Include all files in src folder
}
