from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access_scope import AccessScope
from ...models.list_application_access_scopes_response_400 import ListApplicationAccessScopesResponse400
from ...models.list_application_access_scopes_response_401 import ListApplicationAccessScopesResponse401
from ...models.list_application_access_scopes_response_403 import ListApplicationAccessScopesResponse403
from ...models.list_application_access_scopes_response_404 import ListApplicationAccessScopesResponse404
from ...models.list_application_access_scopes_response_500 import ListApplicationAccessScopesResponse500
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/apps/{id}/access_scopes",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListApplicationAccessScopesResponse400,
        ListApplicationAccessScopesResponse401,
        ListApplicationAccessScopesResponse403,
        ListApplicationAccessScopesResponse404,
        ListApplicationAccessScopesResponse500,
        list["AccessScope"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AccessScope.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListApplicationAccessScopesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListApplicationAccessScopesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListApplicationAccessScopesResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListApplicationAccessScopesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListApplicationAccessScopesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListApplicationAccessScopesResponse400,
        ListApplicationAccessScopesResponse401,
        ListApplicationAccessScopesResponse403,
        ListApplicationAccessScopesResponse404,
        ListApplicationAccessScopesResponse500,
        list["AccessScope"],
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
        ListApplicationAccessScopesResponse400,
        ListApplicationAccessScopesResponse401,
        ListApplicationAccessScopesResponse403,
        ListApplicationAccessScopesResponse404,
        ListApplicationAccessScopesResponse500,
        list["AccessScope"],
    ]
]:
    """List Application Access Scopes

     Get all of the access scopes for a given application.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListApplicationAccessScopesResponse400, ListApplicationAccessScopesResponse401, ListApplicationAccessScopesResponse403, ListApplicationAccessScopesResponse404, ListApplicationAccessScopesResponse500, list['AccessScope']]]
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
        ListApplicationAccessScopesResponse400,
        ListApplicationAccessScopesResponse401,
        ListApplicationAccessScopesResponse403,
        ListApplicationAccessScopesResponse404,
        ListApplicationAccessScopesResponse500,
        list["AccessScope"],
    ]
]:
    """List Application Access Scopes

     Get all of the access scopes for a given application.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListApplicationAccessScopesResponse400, ListApplicationAccessScopesResponse401, ListApplicationAccessScopesResponse403, ListApplicationAccessScopesResponse404, ListApplicationAccessScopesResponse500, list['AccessScope']]
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
        ListApplicationAccessScopesResponse400,
        ListApplicationAccessScopesResponse401,
        ListApplicationAccessScopesResponse403,
        ListApplicationAccessScopesResponse404,
        ListApplicationAccessScopesResponse500,
        list["AccessScope"],
    ]
]:
    """List Application Access Scopes

     Get all of the access scopes for a given application.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListApplicationAccessScopesResponse400, ListApplicationAccessScopesResponse401, ListApplicationAccessScopesResponse403, ListApplicationAccessScopesResponse404, ListApplicationAccessScopesResponse500, list['AccessScope']]]
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
        ListApplicationAccessScopesResponse400,
        ListApplicationAccessScopesResponse401,
        ListApplicationAccessScopesResponse403,
        ListApplicationAccessScopesResponse404,
        ListApplicationAccessScopesResponse500,
        list["AccessScope"],
    ]
]:
    """List Application Access Scopes

     Get all of the access scopes for a given application.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListApplicationAccessScopesResponse400, ListApplicationAccessScopesResponse401, ListApplicationAccessScopesResponse403, ListApplicationAccessScopesResponse404, ListApplicationAccessScopesResponse500, list['AccessScope']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
