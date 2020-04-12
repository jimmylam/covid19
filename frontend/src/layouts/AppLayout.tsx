import React from 'react';
import { Header } from '../components/Header/Header';
const styles = require('../assets/scss/App.scss');

export const AppLayout = ({ children }) => {
return <div>
    <Header />
    { children }
    </div>
}
