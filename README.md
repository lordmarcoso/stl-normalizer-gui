# STL Normalizer GUI

A Windows desktop tool for normalizing ASCII STL files so they open correctly in strict parsers like 3D Evolution, MeshLab, or 3D slicers.

This tool ensures your `.stl` files:
- Start with a valid `solid [name]` header
- End with a proper `endsolid [name]` footer
- Are readable by CAD, MBD, and 3D printing workflows

---

## 🖥 Features

- ✅ Graphical interface (Tkinter)
- ✅ No Python install required (just run the `.exe`)
- ✅ Adds missing headers/footers
- ✅ Does not modify geometry
- ✅ Safe to use on original files (creates a new `_normalized` version)

---

## 📦 How to Use

1. Run `stl_normalizer_gui.exe`
2. Click **“Select File”**
3. Choose your ASCII `.stl` file
4. The tool creates a normalized version:  
   ```
   original_filename_normalized.stl
   ```
5. Load this cleaned version in your target application

---

## 🧪 Before and After

### ❌ Invalid STL (some parsers reject):
```stl
solid
facet normal 0.0 0.0 1.0
  outer loop
    vertex 0.0 0.0 0.0
    vertex 1.0 0.0 0.0
    vertex 1.0 1.0 0.0
  endloop
endfacet
```

### ✅ Normalized STL:
```stl
solid partname
facet normal 0.0 0.0 1.0
  outer loop
    vertex 0.0 0.0 0.0
    vertex 1.0 0.0 0.0
    vertex 1.0 1.0 0.0
  endloop
endfacet
endsolid partname
```

---

## 🚀 Building from Source

This project builds automatically using GitHub Actions.

### Workflow:
- 🪄 `PyInstaller` compiles the `.py` file into a `.exe`
- ⚙️ Flags used: `--onefile --windowed --noupx --clean` for antivirus safety
- ✅ Artifact is uploaded for download

You can trigger a build by pushing changes to `stl_normalizer_gui.py`.

---

## 💡 Notes

- Only supports ASCII `.stl` files (binary not yet supported)
- Doesn’t validate or repair geometry — only header/format
- Safe to use in most engineering or 3D printing pipelines

---

## 🧙 Author

**Lord Marco**  
Crafted for resilient 3D workflows  
Empowering clean data in hostile CAD environments
