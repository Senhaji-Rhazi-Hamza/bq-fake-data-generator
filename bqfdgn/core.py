
def gen_fake_data(fake_config, fake):
    data = []
    for i in range(fake_config['nrows']):
        fake_types = fake_config['fake_types']
        data.append(
            {
                el.get('column_name', None) or el['fake_type']:
                    getattr(fake,el['fake_type'])() if (el.get('kwargs') is None) else getattr(fake,el['fake_type'])(**el.get('kwargs')) 
                    for el in fake_types 
                    }
        )
    return data
