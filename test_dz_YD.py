import pytest
import requests


class TestYD:
    def setup_method(self):
        self.headers = {
            'Authorization': ''
        }

    @pytest.mark.parametrize(
        'param,folder_name,status',
        (
                ('path', 'Folder', 201),
                ('path', 'Folder', 409),
                ('pat', 'F', 400),
        )
    )
    def test_create_folder(self, param, folder_name, status):
        params = {
            param: folder_name
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == status
