import React from 'react';
import { Link } from 'react-router-dom';

export const Header = () => {
    return (
    <div className="flex bg-gray-200">
        <div className="flex-initial text-gray-700 text-center px-4 py-2 m-2">
        <Link to="/">Home</Link>
        </div>
        <div className="flex-initial text-gray-700 text-center px-4 py-2 m-2">
        <Link to="/about">About</Link>
        </div>
  </div>)
}

