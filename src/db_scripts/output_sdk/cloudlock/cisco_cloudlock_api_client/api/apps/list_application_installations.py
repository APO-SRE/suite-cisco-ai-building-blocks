from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apps_collection import AppsCollection
from ...models.list_application_installations_response_400 import ListApplicationInstallationsResponse400
from ...models.list_application_installations_response_401 import ListApplicationInstallationsResponse401
from ...models.list_application_installations_response_403 import ListApplicationInstallationsResponse403
from ...models.list_application_installations_response_404 import ListApplicationInstallationsResponse404
from ...models.list_application_installations_response_500 import ListApplicationInstallationsResponse500
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/apps/{id}/installs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListApplicationInstallationsResponse400,
        ListApplicationInstallationsResponse401,
        ListApplicationInstallationsResponse403,
        ListApplicationInstallationsResponse404,
        ListApplicationInstallationsResponse500,
        list["AppsCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppsCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListApplicationInstallationsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListApplicationInstallationsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListApplicationInstallationsResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListApplicationInstallationsResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListApplicationInstallationsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListApplicationInstallationsResponse400,
        ListApplicationInstallationsResponse401,
        ListApplicationInstallationsResponse403,
        ListApplicationInstallationsResponse404,
        ListApplicationInstallationsResponse500,
        list["AppsCollection"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        ListApplicationInstallationsResponse400,
        ListApplicationInstallationsResponse401,
        ListApplicationInstallationsResponse403,
        ListApplicationInstallationsResponse404,
        ListApplicationInstallationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Installations of Application

     List the application's installations.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListApplicationInstallationsResponse400, ListApplicationInstallationsResponse401, ListApplicationInstallationsResponse403, ListApplicationInstallationsResponse404, ListApplicationInstallationsResponse500, list['AppsCollection']]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        ListApplicationInstallationsResponse400,
        ListApplicationInstallationsResponse401,
        ListApplicationInstallationsResponse403,
        ListApplicationInstallationsResponse404,
        ListApplicationInstallationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Installations of Application

     List the application's installations.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListApplicationInstallationsResponse400, ListApplicationInstallationsResponse401, ListApplicationInstallationsResponse403, ListApplicationInstallationsResponse404, ListApplicationInstallationsResponse500, list['AppsCollection']]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        ListApplicationInstallationsResponse400,
        ListApplicationInstallationsResponse401,
        ListApplicationInstallationsResponse403,
        ListApplicationInstallationsResponse404,
        ListApplicationInstallationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Installations of Application

     List the application's installations.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListApplicationInstallationsResponse400, ListApplicationInstallationsResponse401, ListApplicationInstallationsResponse403, ListApplicationInstallationsResponse404, ListApplicationInstallationsResponse500, list['AppsCollection']]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        ListApplicationInstallationsResponse400,
        ListApplicationInstallationsResponse401,
        ListApplicationInstallationsResponse403,
        ListApplicationInstallationsResponse404,
        ListApplicationInstallationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Installations of Application

     List the application's installations.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListApplicationInstallationsResponse400, ListApplicationInstallationsResponse401, ListApplicationInstallationsResponse403, ListApplicationInstallationsResponse404, ListApplicationInstallationsResponse500, list['AppsCollection']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
