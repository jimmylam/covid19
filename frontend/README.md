# Covid 19 Front End
> Using Tailwind css for styling.

## Installation
1. Clone/download repo
2. `yarn install` (or `npm install` for npm)

## Usage
**Development**

`yarn run start-dev`

**Production**

`yarn run start-prod`

* Build app once (HMR disabled) to `/dist/`
* App served @ `http://localhost:3000`

---

**All commands**

Command | Description
--- | ---
`yarn run start-dev` | Build app continuously (HMR enabled) and serve @ `http://localhost:8080`
`yarn run start-prod` | Build app once (HMR disabled) to `/dist/` and serve @ `http://localhost:3000`
`yarn run build` | Build app to `/dist/`
`yarn run test` | Run tests
`yarn run lint` | Run Typescript linter
`yarn run lint --fix` | Run Typescript linter and fix issues
`yarn run start` | (alias of `yarn run start-dev`)

**Note**: replace `yarn` with `npm` in `package.json` if you use npm.

## See also
* [React Webpack Babel Starter](https://github.com/vikpe/react-webpack-babel-starter)
* [Isomorphic Webapp Starter](https://github.com/vikpe/isomorphic-webapp-starter)
