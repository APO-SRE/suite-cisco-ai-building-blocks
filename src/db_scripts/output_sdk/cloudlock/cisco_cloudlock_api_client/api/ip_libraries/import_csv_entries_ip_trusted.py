from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.import_csv_entries_ip_trusted_response_400 import ImportCsvEntriesIpTrustedResponse400
from ...models.import_csv_entries_ip_trusted_response_401 import ImportCsvEntriesIpTrustedResponse401
from ...models.import_csv_entries_ip_trusted_response_403 import ImportCsvEntriesIpTrustedResponse403
from ...models.import_csv_entries_ip_trusted_response_404 import ImportCsvEntriesIpTrustedResponse404
from ...models.import_csv_entries_ip_trusted_response_500 import ImportCsvEntriesIpTrustedResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    file: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["file"] = file

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ip/trusted",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        ImportCsvEntriesIpTrustedResponse400,
        ImportCsvEntriesIpTrustedResponse401,
        ImportCsvEntriesIpTrustedResponse403,
        ImportCsvEntriesIpTrustedResponse404,
        ImportCsvEntriesIpTrustedResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = ImportCsvEntriesIpTrustedResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ImportCsvEntriesIpTrustedResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ImportCsvEntriesIpTrustedResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ImportCsvEntriesIpTrustedResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ImportCsvEntriesIpTrustedResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Any,
        ImportCsvEntriesIpTrustedResponse400,
        ImportCsvEntriesIpTrustedResponse401,
        ImportCsvEntriesIpTrustedResponse403,
        ImportCsvEntriesIpTrustedResponse404,
        ImportCsvEntriesIpTrustedResponse500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        ImportCsvEntriesIpTrustedResponse400,
        ImportCsvEntriesIpTrustedResponse401,
        ImportCsvEntriesIpTrustedResponse403,
        ImportCsvEntriesIpTrustedResponse404,
        ImportCsvEntriesIpTrustedResponse500,
    ]
]:
    """Import CSV Entries

     Upload a file (IP feed) for review. Use a multipart/form-data request to upload and import a CSV
    file.

    Args:
        file (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImportCsvEntriesIpTrustedResponse400, ImportCsvEntriesIpTrustedResponse401, ImportCsvEntriesIpTrustedResponse403, ImportCsvEntriesIpTrustedResponse404, ImportCsvEntriesIpTrustedResponse500]]
    """

    kwargs = _get_kwargs(
        file=file,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        ImportCsvEntriesIpTrustedResponse400,
        ImportCsvEntriesIpTrustedResponse401,
        ImportCsvEntriesIpTrustedResponse403,
        ImportCsvEntriesIpTrustedResponse404,
        ImportCsvEntriesIpTrustedResponse500,
    ]
]:
    """Import CSV Entries

     Upload a file (IP feed) for review. Use a multipart/form-data request to upload and import a CSV
    file.

    Args:
        file (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImportCsvEntriesIpTrustedResponse400, ImportCsvEntriesIpTrustedResponse401, ImportCsvEntriesIpTrustedResponse403, ImportCsvEntriesIpTrustedResponse404, ImportCsvEntriesIpTrustedResponse500]
    """

    return sync_detailed(
        client=client,
        file=file,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        ImportCsvEntriesIpTrustedResponse400,
        ImportCsvEntriesIpTrustedResponse401,
        ImportCsvEntriesIpTrustedResponse403,
        ImportCsvEntriesIpTrustedResponse404,
        ImportCsvEntriesIpTrustedResponse500,
    ]
]:
    """Import CSV Entries

     Upload a file (IP feed) for review. Use a multipart/form-data request to upload and import a CSV
    file.

    Args:
        file (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImportCsvEntriesIpTrustedResponse400, ImportCsvEntriesIpTrustedResponse401, ImportCsvEntriesIpTrustedResponse403, ImportCsvEntriesIpTrustedResponse404, ImportCsvEntriesIpTrustedResponse500]]
    """

    kwargs = _get_kwargs(
        file=file,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    file: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        ImportCsvEntriesIpTrustedResponse400,
        ImportCsvEntriesIpTrustedResponse401,
        ImportCsvEntriesIpTrustedResponse403,
        ImportCsvEntriesIpTrustedResponse404,
        ImportCsvEntriesIpTrustedResponse500,
    ]
]:
    """Import CSV Entries

     Upload a file (IP feed) for review. Use a multipart/form-data request to upload and import a CSV
    file.

    Args:
        file (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImportCsvEntriesIpTrustedResponse400, ImportCsvEntriesIpTrustedResponse401, ImportCsvEntriesIpTrustedResponse403, ImportCsvEntriesIpTrustedResponse404, ImportCsvEntriesIpTrustedResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            file=file,
        )
    ).parsed
