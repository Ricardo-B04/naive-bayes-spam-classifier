"""
Script para descargar e integrar el dataset SMS Spam Collection
===============================================================

Este script descarga el dataset SMS Spam Collection del UCI Machine Learning
Repository, lo procesa y lo guarda en formato CSV para su uso en el modelo.

El dataset contiene 5,572 mensajes SMS etiquetados como SPAM o HAM (legítimos).
"""

import os
import urllib.request
import zipfile
import pandas as pd
from pathlib import Path


def download_sms_dataset(output_dir='data'):
    """
    Descarga el dataset SMS Spam Collection de UCI.
    
    Args:
        output_dir (str): Directorio donde guardar los datos
        
    Returns:
        str: Ruta al archivo CSV del dataset
    """
    
    # Crear directorio si no existe
    Path(output_dir).mkdir(exist_ok=True)
    
    print("="*60)
    print("DESCARGANDO SMS SPAM COLLECTION DATASET")
    print("="*60 + "\n")
    
    # URL del dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
    zip_path = os.path.join(output_dir, "smsspamcollection.zip")
    extracted_path = os.path.join(output_dir, "SMSSpamCollection")
    csv_path = os.path.join(output_dir, "sms_spam_collection.csv")
    
    # Descargar si no existe
    if not os.path.exists(csv_path):
        
        # Descargar el archivo ZIP
        if not os.path.exists(zip_path):
            print(f"Descargando dataset desde: {url}")
            try:
                urllib.request.urlretrieve(url, zip_path)
                print(f"✓ Archivo descargado: {zip_path}\n")
            except Exception as e:
                print(f"✗ Error al descargar: {e}")
                return None
        
        # Extraer el archivo ZIP
        print("Extrayendo archivos...")
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
            print(f"✓ Archivos extraídos: {extracted_path}\n")
        except Exception as e:
            print(f"✗ Error al extraer: {e}")
            return None
        
        # Procesar el dataset
        print("Procesando dataset...")
        try:
            # El archivo se extrae directamente en el directorio, no en una subcarpeta
            sms_file = os.path.join(output_dir, "SMSSpamCollection")
            
            if not os.path.exists(sms_file):
                print(f"✗ No se encontró el archivo: {sms_file}")
                # Intentar buscar el archivo en el directorio extraído
                for root, dirs, files in os.walk(output_dir):
                    if "SMSSpamCollection" in files:
                        sms_file = os.path.join(root, "SMSSpamCollection")
                        print(f"   Archivo encontrado en: {sms_file}")
                        break
                else:
                    print(f"✗ No se encontró SMSSpamCollection en: {output_dir}")
                    return None
            
            # Leer el archivo
            df = pd.read_csv(
                sms_file,
                sep='\t',
                header=None,
                names=['label', 'text'],
                encoding='utf-8'
            )
            
            # Convertir etiquetas: ham=0, spam=1
            df['label'] = df['label'].apply(lambda x: 1 if x == 'spam' else 0)
            
            # Guardar como CSV
            df.to_csv(csv_path, index=False)
            print(f"✓ Dataset procesado y guardado: {csv_path}\n")
            
            # Limpiar archivos temporales
            os.remove(zip_path)
            
        except Exception as e:
            print(f"✗ Error al procesar: {e}")
            return None
    
    else:
        print(f"Dataset ya existe en: {csv_path}\n")
    
    # Mostrar estadísticas
    print("="*60)
    print("ESTADÍSTICAS DEL DATASET")
    print("="*60)
    
    df = pd.read_csv(csv_path)
    
    print(f"\nTotal de mensajes: {len(df):,}")
    print(f"Mensajes legítimos (HAM): {(df['label'] == 0).sum():,} ({(df['label'] == 0).sum()/len(df)*100:.1f}%)")
    print(f"Mensajes SPAM: {(df['label'] == 1).sum():,} ({(df['label'] == 1).sum()/len(df)*100:.1f}%)")
    
    print(f"\nLongitud promedio de mensajes:")
    print(f"  HAM:  {df[df['label'] == 0]['text'].str.len().mean():.0f} caracteres")
    print(f"  SPAM: {df[df['label'] == 1]['text'].str.len().mean():.0f} caracteres")
    
    print(f"\nEjemplos del dataset:")
    print("-"*60)
    
    # Mostrar ejemplos de SPAM
    spam_example = df[df['label'] == 1]['text'].iloc[0]
    print(f"\nEjemplo SPAM:")
    print(f"  '{spam_example}'")
    
    # Mostrar ejemplos de HAM
    ham_example = df[df['label'] == 0]['text'].iloc[0]
    print(f"\nEjemplo HAM (legítimo):")
    print(f"  '{ham_example}'")
    
    print("\n" + "="*60 + "\n")
    
    return csv_path


if __name__ == "__main__":
    dataset_path = download_sms_dataset()
    
    if dataset_path:
        print(f"✓ ¡Dataset listo para usar en {dataset_path}!")
    else:
        print("✗ Error al descargar el dataset")
