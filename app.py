import extract
import transform
import load

if __name__ == '__main__':
    x = 'https://usc.data.socrata.com/api/views/kygc-fzgm/rows.csv?accessType=DOWNLOAD'
    extracted = extract.extracted_data(x)
    transformed = transform.transform_data(extracted)
    loaded = load.loaded_data(transformed)
   