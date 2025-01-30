import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Dropdown from './Dropdown'
import { Button } from '@mantine/core'

function App() {

  return (
    <>
      <Dropdown />
      <Dropdown />
      <Button>Begin Live Translation</Button>
    </>
  )
}

export default App
