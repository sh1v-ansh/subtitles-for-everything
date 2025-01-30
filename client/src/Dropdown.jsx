import { Menu, Button } from '@mantine/core';

function BasicDropdown() {
  
  const languages = ["English", "French", "German"]
  
  return (
    <Menu shadow="md" width={200}>
      <Menu.Target>
        <Button>Open Dropdown</Button>
      </Menu.Target>

      <Menu.Dropdown>
        {languages.map((language) => (
          <Menu.Item key={language} onClick={() => alert(`Clicked ${language}`)}>
            {language}
          </Menu.Item>
        ))}
      </Menu.Dropdown>
    </Menu>
  );
}

export default BasicDropdown;